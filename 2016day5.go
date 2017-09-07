package main

import "fmt"
import "crypto/md5"
import "os"
import "strconv"

type AnswerPair struct {
	Position byte
	OutputChar byte
}

func main() {
	input := []byte(os.Args[1])
	const threads = 4
	testInts := make(chan int64, threads)
	answers := make(chan AnswerPair, threads)
	for i := int64(0); i < threads; i++ {
		go checkInts(input, testInts, answers)
	}

	go func() {
		answer := make([]byte, 8)
		for {
			pair := <-answers
			if answer[pair.Position] != 0 {
				continue
			}
			answer[pair.Position] = pair.OutputChar
			numAnswers := 0
			for _, b := range(answer) {
				if b == 0 {
					fmt.Print("_")
				} else {
					fmt.Printf("%c", b)
					numAnswers += 1
				}
			}
			fmt.Println()
			if numAnswers == 8 {
				os.Exit(0)
			}
		}
	}()

	for i := int64(0); ; i++ {
		testInts <-i
	}
}

const maxInt = int64(^uint64(0) >> 1)

func checkInts(input []byte, testInts chan int64, answers chan AnswerPair) {
	maxIntLen := len(strconv.FormatInt(maxInt, 10))
	test := make([]byte, 0, len(input) + maxIntLen)
	test = append(test, input...)
	buffer := make([]byte, maxIntLen)
	for {
		testInt := <-testInts
		//test := strconv.AppendInt(buffer, testInt, 10)
		test = formatBits(test, len(input), buffer, uint64(testInt), testInt < 0)
		//fmt.Printf("testing %s %d %d\n", test, len(test), cap(test))
		hash := md5.Sum(test)
		if hash[0] == 0 && hash[1] == 0 && hash[2] & 0xf0 == 0 {
			position := hash[2] & 0x0f
			if position < 8 {
				outputChar := strconv.FormatUint(uint64(hash[3] & 0xf0), 16)[0]
				answers <- AnswerPair{position, outputChar}
			}
		}
	}
}


// mostly copied from strconv/itoa.go
func formatBits(dst []byte, offset int, buffer []byte, u uint64, neg bool) []byte {
	i := len(buffer)
	if neg {
		u = -u
	}

	// u guaranteed to fit into a uintptr
	us := uintptr(u)
	for us >= 10 {
		i--
		q := us / 10
		buffer[i] = byte(us - q*10 + '0')
		us = q
	}
	// u < 10
	i--
	buffer[i] = byte(us + '0')
	// add sign, if any
	if neg {
		i--
		buffer[i] = '-'
	}

	intLen := len(buffer) - i
	dst = dst[0:offset + intLen]
	start := i
	for ; i < len(buffer); i++ {
		dst[offset + i - start] = buffer[i]
	}
	return dst
}
