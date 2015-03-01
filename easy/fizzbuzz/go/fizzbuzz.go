package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parse_input() [][]int {
	var err error
	in_source := os.Stdin
	if len(os.Args) > 1 {
		in_source, err = os.Open(os.Args[1])
		if err != nil {
			panic(err)
		}
	}

	var input [][]int
	scanner := bufio.NewScanner(in_source)
	for scanner.Scan() {
		var line []int
		for _, value := range strings.Split(scanner.Text(), " ") {
			value_to_int, _ := strconv.Atoi(value)
			line = append(line, value_to_int)
		}
		input = append(input, line)
	}

	return input
}

func fizzbuzz(input []int) []string {
	fizz_a := input[0]
	fizz_b := input[1]
	stop := input[2]
	var fb []string
	for i := 1; i <= stop; i++ {
		var buffer bytes.Buffer
		if i%fizz_a == 0 {
			buffer.WriteString("Fizz")
		}
		if i%fizz_b == 0 {
			buffer.WriteString("Buzz")
		}
		if buffer.Len() == 0 {
			buffer.WriteString(strconv.Itoa(i))
		}
		fb = append(fb, buffer.String())
	}
	return fb
}

func main() {
	input := parse_input()
	for _, line := range input {
		output := fizzbuzz(line)

		for i := 0; i < len(output); i++ {
			fmt.Println(output[i])
		}
	}
}
