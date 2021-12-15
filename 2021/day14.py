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
	part1()
