#!/usr/bin/env python3

import utils

def part1():
	paper, folds = parse_input()
	paper = fold(paper, *folds[0])
	print(sum(row.count('#') for row in paper))

def part2():
	paper, folds = parse_input()
	for fold_inst in folds:
		paper = fold(paper, *fold_inst)
	print_paper(paper)

def parse_input():
	dots = []
	max_x = max_y = 0
	folds = []
	reading_folds = False
	for line in utils.iter_lines(13):
		if not reading_folds and line == '':
			reading_folds = True
		elif not reading_folds:
			x, y = map(int, line.split(','))
			dots.append((x, y))
			if x > max_x:
				max_x = x
			if y > max_y:
				max_y = y
		else:
			_, instr = line.split('fold along ')
			axis, pos = instr.split('=')
			folds.append((axis, int(pos)))

	paper = [['.'] * (max_x + 1) for _ in range(max_y + 1)]
	for x, y in dots:
		paper[y][x] = '#'
	return paper, folds

def fold(paper, axis, pos):
	if axis == 'y':
		axis_len = len(paper)
		cross_len = len(paper[0])
		new_paper = [['.'] * cross_len for _ in range(pos)]
		for y1, y2 in enumerate(range(axis_len-1, pos, -1)):
			for x, (dot1, dot2) in enumerate(zip(paper[y1], paper[y2])):
				if '#' in (dot1, dot2):
					new_paper[y1][x] = '#'
				else:
					new_paper[y1][x] = '.'
	else:
		assert axis == 'x'
		axis_len = len(paper[0])
		cross_len = len(paper)
		new_paper = [['.'] * pos for _ in range(cross_len)]
		for x1, x2 in enumerate(range(axis_len-1, pos, -1)):
			for y, row in enumerate(paper):
				if '#' in (row[x1], row[x2]):
					new_paper[y][x1] = '#'
				else:
					new_paper[y][x1] = '.'
	return new_paper

def print_paper(paper):
	for row in paper:
		print(''.join(row))

if __name__ == '__main__':
	part2()
