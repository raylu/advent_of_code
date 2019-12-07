#!/usr/bin/env python3

import fileinput

def main():
	tree = {}
	for line in fileinput.input():
		left, right = line.rstrip().split(')', 1)
		tree[right] = left

	you_path = list(path_to_root(tree, tree['YOU']))
	you_path_nodes = frozenset(you_path)
	for i, node in enumerate(path_to_root(tree, tree['SAN'])):
		if node in you_path_nodes:
			print(i + you_path.index(node))
			break
	else:
		raise AssertionError()

def path_to_root(tree, node):
	while node != 'COM':
		yield node
		node = tree[node]

if __name__ == '__main__':
	main()
