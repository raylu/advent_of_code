#!/usr/bin/env python3

import utils

WINDOW_SIZE = 3

def part2():
	increases = 0
	prev = []
	prev_sum = None
	for line in utils.iter_lines(1):
		cur = int(line.rstrip())
		if len(prev) < WINDOW_SIZE - 1:
			prev.append(cur)
			continue

		cur_sum = sum(prev) + cur
		if prev_sum is not None and cur_sum > prev_sum:
			increases += 1

		prev.pop(0)
		prev.append(cur)
		prev_sum = cur_sum
	print(increases)

if __name__ == '__main__':
	part2()
