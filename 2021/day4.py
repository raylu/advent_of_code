#!/usr/bin/env python3

import utils

def part1():
	line_iter = utils.iter_lines(4)
	draw = list(map(int, next(line_iter).split(',')))
	boards = []
	while True:
		try:
			assert next(line_iter) == ''
		except StopIteration:
			break
		board = [list(map(int, next(line_iter).split())) for _ in range(5)]
		boards.append(board)

	board_states = []
	for _ in range(len(boards)):
		board_state = [[False] * 5 for _ in range(5)]
		board_states.append(board_state)

	winner = None
	for num in draw:
		print(num)
		for board_idx, board in enumerate(boards):
			for row_idx, row in enumerate(board):
				try:
					col_idx = row.index(num)
				except ValueError:
					continue
				board_states[board_idx][row_idx][col_idx] = True

				if sum(board_states[board_idx][row_idx]) == 5 or \
						sum(row[col_idx] for row in board_states[board_idx]) == 5:
					winner = board_idx
				break
			if winner:
				break
		if winner:
			break
	final_num = num

	print('winner: board', winner)
	board_sum = 0
	for row_num, row in enumerate(boards[winner]):
		for col_num, num in enumerate(row):
			if not board_states[winner][row_num][col_num]:
				board_sum += num
	print(board_sum, final_num, board_sum * final_num)

if __name__ == '__main__':
	part1()
