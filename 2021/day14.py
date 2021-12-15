#!/usr/bin/env python3

import collections
import operator

import utils

def part1():
	s, rules = parse_input()
	for _ in range(10):
		s = step(rules, s)

	counter = collections.Counter(s)
	(_, most), = counter.most_common(1)
	_, least = sorted(counter.items(), key=operator.itemgetter(1))[0]
	print(most - least)

def part2():
	s, rules = parse_input()
	pairs = collections.defaultdict(int)
	for i in range(len(s) - 1):
		pairs[s[i] + s[i+1]] += 1

	for _ in range(40):
		new = collections.defaultdict(int)
		for pair, count in pairs.items():
			left, right = pair
			middle = rules[pair]
			new[left + middle] += count
			new[middle + right] += count
		pairs = new

	counter = collections.defaultdict(int)
	for pair, count in pairs.items():
		for c in pair:
			counter[c] += count / 2
	counter[s[0]] += 0.5
	counter[s[-1]] += 0.5
	counts = sorted(counter.items(), key=operator.itemgetter(1))
	print(counts[-1][1] - counts[0][1])

def parse_input():
	line_iter = utils.iter_lines(14)
	template = next(line_iter)
	assert next(line_iter) == ''
	rules = []
	for line in line_iter:
		pair, elem = line.split(' -> ')
		rules.append((pair, elem))
	return template, dict(rules)

def step(rules, s):
	new = ''
	for i in range(len(s) - 1):
		new += s[i]
		new += rules[s[i] + s[i+1]]
	new += s[-1]
	return new

if __name__ == '__main__':
	part2()
