#!/usr/bin/env python3

WINDOW_SIZE = 3

def main():
	increases = 0
	with open('day1_input', 'r', encoding='ascii') as f:
		prev = []
		prev_sum = None
		for line in f:
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
	main()
