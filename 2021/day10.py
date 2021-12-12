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
		illegal, _ = illegal_or_complete(line)
		if illegal is not None:
			score += points[illegal]
	print(score)

def part2():
	points = {
		')': 1,
		']': 2,
		'}': 3,
		'>': 4,
	}
	scores = []
	for line in utils.iter_lines(10):
		_, stack = illegal_or_complete(line)
		if stack is None:
			continue
		score = 0
		while stack:
			c = stack.pop()
			score = score * 5 + points[c]
		scores.append(score)
	scores.sort()
	print(scores[len(scores) // 2])

def illegal_or_complete(line):
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
			return c, None
	return None, stack

if __name__ == '__main__':
	part2()
