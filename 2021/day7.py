#!/usr/bin/env python3

import utils

def part1():
	positions = utils.read_int_line(7)
	max_pos = max(positions)
	min_cost = float('inf')
	for i in range(1, max_pos):
		fuel = 0
		for pos in positions:
			fuel += abs(pos - i)

		if fuel < min_cost:
			print('new min', fuel)
			min_cost = fuel

def part2():
	positions = utils.read_int_line(7)
	max_pos = max(positions)
	min_cost = float('inf')
	for i in range(1, max_pos):
		fuel = 0
		for pos in positions:
			distance = abs(pos - i)
			fuel += distance * (distance + 1) // 2

		if fuel < min_cost:
			print('new min', fuel)
			min_cost = fuel

if __name__ == '__main__':
	part2()
