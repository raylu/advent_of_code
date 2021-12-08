#!/usr/bin/env python3

import utils

def part1():
	total = 0
	for line in utils.iter_lines(8):
		patterns, output = line.split('|')
		output_digits = output.split()
		total += sum(1 for output_digit in output_digits if len(output_digit) in (2, 3, 4, 7))
	print(total)

if __name__ == '__main__':
	part1()
