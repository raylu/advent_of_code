#!/usr/bin/env python3

import utils

def part1():
	zeroes = [0] * 12
	ones = [0] * 12
	for line in utils.iter_lines(3):
		for i, bit in enumerate(line):
			if bit == '0':
				zeroes[i] += 1
			elif bit == '1':
				ones[i] += 1
			else:
				raise AssertionError('got line ' + line)

	gamma = epsilon = 0
	for i, (num_zeroes, num_ones) in enumerate(zip(reversed(zeroes), reversed(ones))):
		if num_zeroes > num_ones:
			epsilon |= 1 << i
		elif num_zeroes < num_ones:
			gamma |= 1 << i
		else:
			raise AssertionError(f'{num_zeroes} == {num_ones} at {i}')
	print(gamma, epsilon, gamma * epsilon)

def part2():
	lines = list(utils.iter_lines(3))
	oxygen = find_value(lines, True, '1')
	co2 = find_value(lines, False, '0')
	print(oxygen, co2, oxygen * co2)

def find_value(lines, keep_more, fallback):
	pos = 0
	while len(lines) > 1:
		lines = filter_lines(lines, pos, keep_more, fallback)
		pos += 1
	(line,) = lines
	return int(line, 2)

def filter_lines(lines, pos, keep_more, fallback):
	zeroes = ones = 0
	for line in lines:
		if line[pos] == '0':
			zeroes += 1
		elif line[pos] == '1':
			ones += 1
		else:
			raise AssertionError('got line ' + line)

	if zeroes == ones:
		keep = fallback
	elif (zeroes > ones and keep_more) or (zeroes < ones and not keep_more):
		keep = '0'
	else:
		keep = '1'
	return [line for line in lines if line[pos] == keep]

if __name__ == '__main__':
	part2()
