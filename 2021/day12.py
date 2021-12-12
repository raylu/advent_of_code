#!/usr/bin/env python3

import collections

import utils

def part1():
	graph = collections.defaultdict(list)
	for line in utils.iter_lines(12):
		node1, node2 = line.split('-')
		graph[node1].append(node2)
		graph[node2].append(node1)

	smalls = set(['start'])
	print(paths(graph, smalls, 'start'))

def paths(graph, smalls, node):
	subpaths = 0
	for dest in graph[node]:
		if dest == 'end':
			subpaths += 1
			continue

		is_small = dest == dest.lower()
		if is_small:
			if dest in smalls:
				continue
			subpaths += paths(graph, smalls | {dest}, dest)
		else:
			subpaths += paths(graph, smalls, dest)
	return subpaths

if __name__ == '__main__':
	part1()
