package main

import "fmt"
import "crypto/md5"
import "os"
import "strconv"


func main() {
	input := []byte(os.Args[1])
	testInts := make(chan int64)
	const threads = 1
	answers := make(chan byte, threads)
	for i := int64(0); i < threads; i++ {
		go checkInts(input, testInts, answers)
	}

	answer := make([]byte, 8)
	numAnswers := 0
	loop:
	for i := int64(0); ; i++ {
		select {
		case outputChar := <-answers:
			answer[numAnswers] = outputChar
			numAnswers++
			fmt.Printf("%s\n", answer)
			if numAnswers == 8 {
				break loop
			}
		default:
		}
		testInts <-i
	}
}

func checkInts(input []byte, testInts chan int64, answers chan byte) {
	for {
		testInt := <-testInts
		test := strconv.AppendInt(input, testInt, 10)
		hash := md5.Sum(test)
		if hash[0] == 0 && hash[1] == 0 && hash[2] & 0xf0 == 0 {
			outputChar := strconv.FormatUint(uint64(hash[2] & 0x0f), 16)[0]
			answers <- outputChar
		}
	}
}
