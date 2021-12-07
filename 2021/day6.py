#!/usr/bin/env python3


def part1():
	with open('day6_input', 'r', encoding='ascii') as f:
		state = list(map(int, f.read().rstrip().split(',')))

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

if __name__ == '__main__':
	part1()
