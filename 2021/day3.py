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

if __name__ == '__main__':
	part1()
