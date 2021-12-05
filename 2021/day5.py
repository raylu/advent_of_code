#!/usr/bin/env python3

import utils

def part1():
	print(count_overlaps(False))

def part2():
	print(count_overlaps(True))

def count_overlaps(diagonals: bool):
	grid = [[0] * 1000 for _ in range(1000)]
	for line in utils.iter_lines(5):
		start, end = line.split(' -> ')
		x1, y1 = map(int, start.split(','))
		x2, y2 = map(int, end.split(','))
		if x1 == x2:
			x = x1
			for y in range(min(y1, y2), max(y1, y2)+1):
				grid[x][y] += 1
		elif y1 == y2:
			y = y1
			for x in range(min(x1, x2), max(x1, x2)+1):
				grid[x][y] += 1
		elif diagonals:
			dx = dy = 1
			if x1 > x2:
				dx = -1
			if y1 > y2:
				dy = -1
			for x, y in zip(range(x1, x2+dx, dx), range(y1, y2+dy, dy)):
				grid[x][y] += 1

	overlaps = 0
	for row in grid:
		overlaps += sum(1 for cell in row if cell >= 2)
	return overlaps

if __name__ == '__main__':
	part2()
