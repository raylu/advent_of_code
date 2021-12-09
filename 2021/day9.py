#!/usr/bin/env python3

import functools
import operator

import utils

cardinal_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def part1():
	grid = [list(map(int, line)) for line in utils.iter_lines(9)]
	risk_level = 0
	for i, j in iter_basins(grid):
		risk_level += grid[i][j] + 1
	print(risk_level)

def part2():
	grid = [list(map(int, line)) for line in utils.iter_lines(9)]
	basin_sizes = []
	for i, j in iter_basins(grid):
		seen = set()
		find_basin(grid, i, j, seen)
		basin_sizes.append(len(seen))

	basin_sizes.sort()
	print(basin_sizes)
	print(functools.reduce(operator.mul, basin_sizes[-3:], 1))

def iter_basins(grid):
	for i, row in enumerate(grid):
		for j, c in enumerate(row):
			for di, dj in cardinal_directions:
				if in_bounds(grid, i + di, j + dj) and grid[i+di][j+dj] <= c:
					break
			else: # low point
				yield i, j

def in_bounds(grid, i, j):
	return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def find_basin(grid, i, j, seen):
	for di, dj in cardinal_directions:
		new_coords = i + di, j + dj
		if new_coords not in seen and in_bounds(grid, *new_coords) and grid[i+di][j+dj] != 9:
			seen.add(new_coords)
			find_basin(grid, *new_coords, seen)

if __name__ == '__main__':
	part2()
