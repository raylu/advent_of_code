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

func checkInts(input []byte, testInts chan int64, answers chan AnswerPair) {
	for {
		testInt := <-testInts
		test := strconv.AppendInt(input, testInt, 10)
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
