#!/usr/bin/env python3

import collections

def part1():
	state = read_state()
	for _ in range(80):
		new_state = []
		for i, fish in enumerate(state):
			if fish == 0:
				new_state.append(8)
				new_state.append(6)
			else:
				new_state.append(fish-1)
		state = new_state
	print(len(state))

def part2():
	state = read_state()
	fish_counts = collections.Counter(state)
	for _ in range(256):
		new_counts = {}
		new_sixes = 0
		for stage, num in fish_counts.items():
			if stage == 0:
				new_counts[8] = num
				new_sixes = num
			else:
				new_counts[stage - 1] = num
		new_counts.setdefault(6, 0)
		new_counts[6] += new_sixes
		fish_counts = new_counts
	print(sum(new_counts.values()))

def read_state():
	with open('day6_input', 'r', encoding='ascii') as f:
		return list(map(int, f.read().rstrip().split(',')))

if __name__ == '__main__':
	part2()
