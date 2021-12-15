#!/usr/bin/env python3

import heapq

import utils

def part1():
	cave = [list(map(int, line)) for line in utils.iter_lines(15)]
	print(min_risk(cave))

def part2():
	cave = [list(map(int, line)) for line in utils.iter_lines(15)]
	width = len(cave[0])
	height = len(cave)
	big_cave = [[0] * width * 5 for _ in range(height * 5)]
	for tile_y in range(5):
		for tile_x in range(5):
			modifier = tile_x + tile_y
			for y in range(height):
				for x in range(width):
					val = cave[y][x] + modifier
					while val > 9:
						val -= 9
					big_cave[tile_y * height + y][tile_x * width + x] = val
	print(min_risk(big_cave))

def min_risk(cave):
	width = len(cave[0])
	height = len(cave)
	goal = (width-1, height-1)

	path = {}
	g_score = {(0, 0): 0}
	f_score = {(0, 0): width + height}
	open_set = list(f_score.items())
	while open_set:
		current, score = heapq.heappop(open_set)
		if current == goal:
			break
		for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
			x, y = current[0] + dx, current[1] + dy
			if 0 <= x < width and 0<= y < height:
				tentative_gscore = g_score[current] + cave[y][x]
				neighbor = (x, y)
				if tentative_gscore < g_score.get(neighbor, float('inf')):
					path[neighbor] = current
					g_score[neighbor] = tentative_gscore
					neighbor_f_score = tentative_gscore + (width - x) + (height - y)
					f_score[neighbor] = neighbor_f_score
					if not any(coord == neighbor for coord, _ in open_set):
						heapq.heappush(open_set, (neighbor, neighbor_f_score))
	
	risk = 0
	while current in path:
		x, y = current
		risk += cave[y][x]
		current = path[current]
	return risk

if __name__ == '__main__':
	part2()
