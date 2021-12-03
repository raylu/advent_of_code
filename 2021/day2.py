#!/usr/bin/env python3

import utils

def part1():
	horizontal = depth = 0
	for line in utils.iter_lines(2):
		command, num = line.rstrip().split()
		num = int(num)
		if command == 'forward':
			horizontal += num
		elif command == 'down':
			depth += num
		elif command == 'up':
			depth -= num
	print(horizontal, depth, horizontal * depth)

if __name__ == '__main__':
	part1()
