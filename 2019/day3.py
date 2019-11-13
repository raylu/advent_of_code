#!/usr/bin/env python3

import fileinput

def main():
	with fileinput.input() as f:
		wire1 = next(f).rstrip().split(',')
		wire2 = next(f).rstrip().split(',')

	seen = {}
	for steps, coord in enumerate(coords(wire1)):
		seen[coord] = steps + 1

	min_steps = float('inf')
	for steps, coord in enumerate(coords(wire2)):
		wire1_steps = seen.get(coord)
		if wire1_steps is not None:
			steps += 1 + wire1_steps
			min_steps = min(steps, min_steps)
	print(min_steps)

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
