#!/usr/bin/env python3

import collections
import fileinput

def main():
	tree = collections.defaultdict(list)
	for line in fileinput.input():
		left, right = line.rstrip().split(')', 1)
		tree[left].append(right)

	print(count_orbits(tree, 'COM', 0))

def count_orbits(tree, node, depth):
	total = depth
	for children in tree[node]:
		total += count_orbits(tree, children, depth + 1)
	return total

if __name__ == '__main__':
	main()
