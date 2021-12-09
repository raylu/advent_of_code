#!/usr/bin/env python3

import operator

import utils

def part1():
	grid = [list(map(int, line)) for line in utils.iter_lines(9)]
	risk_level = 0
	for i, row in enumerate(grid):
		for j, c in enumerate(row):
			for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
				if 0 <= i + di < len(grid) and 0 <= j + dj < len(row) and \
						grid[i+di][j+dj] <= c:
					break
			else: # low point
				risk_level += c + 1
	print(risk_level)

if __name__ == '__main__':
	part1()
