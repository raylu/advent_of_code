#!/usr/bin/env python3

import collections

import utils

def part1():
	graph = read_graph()
	print(paths_1(graph, set(['start']), 'start'))

def part2():
	graph = read_graph()
	print(paths_2(graph, set(['start']), 'start', None))

def read_graph():
	graph = collections.defaultdict(list)
	for line in utils.iter_lines(12):
		node1, node2 = line.split('-')
		graph[node1].append(node2)
		graph[node2].append(node1)
	return graph

def paths_1(graph, smalls, node):
	subpaths = 0
	for dest in graph[node]:
		if dest == 'end':
			subpaths += 1
			continue

		is_small = dest == dest.lower()
		if is_small:
			if dest in smalls:
				continue
			subpaths += paths_1(graph, smalls | {dest}, dest)
		else:
			subpaths += paths_1(graph, smalls, dest)
	return subpaths

def paths_2(graph, smalls, node, twice):
	subpaths = 0
	for dest in graph[node]:
		if dest == 'end':
			subpaths += 1
			continue
		elif dest == 'start':
			continue

		is_small = dest == dest.lower()
		if is_small:
			if dest in smalls:
				if twice is None:
					subpaths += paths_2(graph, smalls, dest, dest)
			else:
				subpaths += paths_2(graph, smalls | {dest}, dest, twice)
		else:
			subpaths += paths_2(graph, smalls, dest, twice)
	return subpaths


if __name__ == '__main__':
	part2()
