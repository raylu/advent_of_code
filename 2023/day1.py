#!/usr/bin/env python3

import typing

def main():
	with open('day1_input', 'r') as f:
		lines = f.read().splitlines()

	total = 0
	for line in lines:
		total += int(first_num(line) + first_num(reversed(line)))
	print(total)

def first_num(line: typing.Sequence[str]) -> str:
	for c in line:
		if c.isdigit():
			return c

if __name__ == '__main__':
	main()
