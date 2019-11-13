#!/usr/bin/env python3

import fileinput
import functools

def main():
	total = 0
	for line in fileinput.input():
		weight = int(line.rstrip())
		total += fuel_req(weight)
	print(total)

@functools.lru_cache()
def fuel_req(weight):
	fuel = weight // 3 - 2
	if fuel <= 0:
		return 0
	fuel += fuel_req(fuel)
	return fuel

if __name__ == '__main__':
	main()
