#!/usr/bin/env python3

import functools
import operator

import utils

cardinal_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def part1():
	points = {
		')': 3,
		']': 57,
		'}': 1197,
		'>': 25137,
	}
	score = 0
	for line in utils.iter_lines(10):
		illegal = find_illegal(line)
		if illegal is not None:
			score += points[illegal]
	print(score)

def find_illegal(line):
	stack = []
	for c in line:
		if c == '(':
			stack.append(')')
		elif c == '[':
			stack.append(']')
		elif c == '{':
			stack.append('}')
		elif c == '<':
			stack.append('>')
		elif stack.pop() != c:
			return c

if __name__ == '__main__':
	part1()
