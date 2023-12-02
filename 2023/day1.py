#!/usr/bin/env python3

def main():
	with open('day1_input', 'r') as f:
		lines = f.read().splitlines()

	total = 0
	for line in lines:
		total += int(first_num(line) + last_num(line))
	print(total)

DIGITS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def first_num(line: str) -> str:
	for i, c in enumerate(line):
		if c.isdigit():
			return c
		for j, digit in enumerate(DIGITS):
			if line[i:].startswith(digit):
				return str(j+1)
	raise AssertionError

def last_num(line: str) -> str:
	for i in range(len(line) - 1, -1, -1):
		if line[i].isdigit():
			return line[i]
		for j, digit in enumerate(DIGITS):
			if line[i:].startswith(digit):
				return str(j+1)
	raise AssertionError

if __name__ == '__main__':
	main()
