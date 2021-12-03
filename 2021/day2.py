#!/usr/bin/env python3

def main():
	horizontal = depth = 0
	with open('day2_input', 'r', encoding='ascii') as f:
		for line in f:
			command, num = line.rstrip().split()
			num = int(num)
			if command == 'forward':
				horizontal += num
			elif command == 'down':
				depth += num
			elif command == 'up':
				depth -= num
	print(horizontal, depth, horizontal * depth)

if __name__ == '__main__':
	main()
