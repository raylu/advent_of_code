#!/usr/bin/env python3

import copy
import fileinput

def main():
	with fileinput.input() as f:
		original_prog = list(map(int, next(f).split(',')))
	for noun in range(0, 100):
		for verb in range(0, 100):
			prog = copy.copy(original_prog)
			prog[1] = noun
			prog[2] = verb
			try:
				run(prog)
			except AssertionError:
				continue
			if prog[0] == 19690720:
				print(noun, verb)
				break

def run(prog):
	pc = 0
	while prog[pc] != 99:
		opcode = prog[pc]
		assert opcode in (1, 2)
		pos1, pos2, output_pos = prog[pc+1:pc+4]
		input1, input2 = prog[pos1], prog[pos2]
		if opcode == 1:
			output = input1 + input2
		elif opcode == 2:
			output = input1 * input2
		prog[output_pos] = output
		pc += 4

if __name__ == '__main__':
	main()
