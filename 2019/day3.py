#!/usr/bin/env python3

import fileinput

def main():
	with fileinput.input() as f:
		wire1 = next(f).rstrip().split(',')
		wire2 = next(f).rstrip().split(',')

	seen = frozenset(coords(wire1))
	min_dist = float('inf')
	for x, y in coords(wire2):
		if (x, y) in seen:
			dist = abs(x) + abs(y)
			min_dist = min(dist, min_dist)
	print(min_dist)

def coords(wire):
	x = y = 0
	for ins in wire:
		direction = ins[0]
		assert direction in 'UDLR'
		count = int(ins[1:])
		for _ in range(count):
			if direction == 'U':
				y -= 1
			elif direction == 'D':
				y += 1
			elif direction == 'L':
				x -= 1
			elif direction == 'R':
				x += 1
			yield x, y

if __name__ == '__main__':
	main()
