#!/usr/bin/env python3

import utils

cardinal_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def part1():
	octopi = [list(map(int, line)) for line in utils.iter_lines(11)]
	flashes = 0
	for _ in range(100):
		flashes += step(octopi)
	print(flashes)

directions = [
	( 0,  1),
	( 1,  0),
	( 0, -1),
	(-1,  0),
	( 1,  1),
	(-1,  1),
	( 1, -1),
	(-1, -1),
]

def step(octopi):
	flashed = []
	for i, line in enumerate(octopi):
		for j, energy in enumerate(line):
			if energy == 9:
				flashed.append((i, j))
			octopi[i][j] = energy + 1

	for i, j in flashed:
		for di, dj in directions:
			new_i, new_j = i + di, j + dj
			if (new_i, new_j) not in flashed and 0 <= new_i < 10 and 0 <= new_j < 10:
				octopi[new_i][new_j] += 1
				if octopi[new_i][new_j] > 9:
					flashed.append((new_i, new_j))
		octopi[i][j] = 0
	return len(flashed)

if __name__ == '__main__':
	part1()
