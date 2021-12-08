#!/usr/bin/env python3

import operator

import utils

def part1():
	total = 0
	for line in utils.iter_lines(8):
		patterns, output = line.split('|')
		output_digits = output.split()
		total += sum(1 for output_digit in output_digits if len(output_digit) in (2, 3, 4, 7))
	print(total)

def part2():
	total = 0
	for line in utils.iter_lines(8):
		patterns, output = map(operator.methodcaller('split'), line.split('|'))
		digits = {}
		pattern_one = None
		fives = []
		sixes = []
		for pattern in patterns:
			pattern_len = len(pattern)
			if pattern_len == 2:
				pattern_one = pattern
				digits[pattern] = 1
			elif pattern_len == 3:
				digits[pattern] = 7
			elif pattern_len == 4:
				digits[pattern] = 4
			elif pattern_len == 5:
				fives.append(pattern)
			elif pattern_len == 6:
				sixes.append(pattern)
			elif pattern_len == 7:
				digits[pattern] = 8

		pattern_six = None
		for pattern in sixes:
			if pattern.count(pattern_one[0]) + pattern.count(pattern_one[1]) == 1:
				pattern_six = pattern
				digits[pattern] = 6
				break
		else:
			raise AssertionError('no six in ' + line)
		c_wires = set(pattern_one)
		(c_wire,) = c_wires.difference(pattern_six)
		(f_wire,) = c_wires.difference(c_wire)

		pattern_five = None
		for pattern in fives:
			c_count = pattern.count(c_wire)
			f_count = pattern.count(f_wire)
			if c_count == 1 and f_count == 0:
				digits[pattern] = 2
			elif c_count == 1 and f_count == 1:
				digits[pattern] = 3
			elif c_count == 0 and f_count == 1:
				pattern_five = pattern
				digits[pattern] = 5

		pattern_nine = set(pattern_five + c_wire)
		sixes.remove(pattern_six)
		for pattern in sixes:
			if set(pattern) == pattern_nine:
				digits[pattern] = 9
			else:
				digits[pattern] = 0

		sorted_digits = {''.join(sorted(k)): v for k, v in digits.items()}
		decoded = 0
		for i, pattern in enumerate(output):
			decoded += sorted_digits[''.join(sorted(pattern))] * 10 ** (3-i)
		total += decoded
	print(total)

if __name__ == '__main__':
	part2()
