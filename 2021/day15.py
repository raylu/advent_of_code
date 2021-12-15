#!/usr/bin/env python3

import heapq

import utils

def part1():
	cave = [list(map(int, line)) for line in utils.iter_lines(15)]
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
		current = path[current]
		x, y = current
		risk += cave[y][x]
	print(risk)

if __name__ == '__main__':
	part1()
