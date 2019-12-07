#!/usr/bin/env python3

import copy
import enum
import fileinput
import itertools
import queue
import threading

def main():
	original_prog = []
	for line in fileinput.input():
		line = line.rstrip(',\n')
		if line:
			original_prog.extend(map(int, line.split(',')))

	max_signal = float('-inf')
	for phase_settings in itertools.permutations([5, 6, 7, 8, 9]):
		signal = test(original_prog, phase_settings)
		max_signal = max(signal, max_signal)
	print(max_signal)

def test(original_prog, phase_settings):
	input_queue = queue.Queue()
	output_queue = queue.Queue()
	programs = []
	for _ in phase_settings[:-1]:
		programs.append(Program(copy.copy(original_prog), input_queue, output_queue))
		input_queue = output_queue
		output_queue = queue.Queue()
	programs.append(Program(copy.copy(original_prog), input_queue, programs[0].input_queue))
	for program in programs:
		thread = threading.Thread(target=program.run)
		thread.start()
	for program, phase_setting in zip(programs, phase_settings):
		program.input_queue.put(phase_setting)
	programs[0].input_queue.put(0)
	thread.join()
	return programs[-1].output_queue.get_nowait()

@enum.unique
class Op(enum.IntEnum):
	ADD = 1
	MUL = 2
	INP = 3
	OUT = 4
	JIT = 5
	JIF = 6
	ILT = 7
	IEQ = 8

class Param:
	def __init__(self, mode, val, pos=None):
		self.mode = mode
		self.val = val
		if pos is not None:
			self.pos = pos

class Program:
	def __init__(self, prog, input_queue, output_queue):
		self.prog = prog
		self.input_queue = input_queue
		self.output_queue = output_queue

	def run(self):
		pc = 0
		while self.prog[pc] != 99:
			opcode = self.prog[pc]
			param_modes, op = divmod(opcode, 100)
			op = Op(op)

			if op in (Op.ADD, Op.MUL, Op.ILT, Op.IEQ):
				n_params = 3
			elif op in (Op.INP, Op.OUT):
				n_params = 1
			elif op in (Op.JIT, Op.JIF):
				n_params = 2
			else:
				raise AssertionError(opcode)

			params = []
			for i in range(n_params):
				param_modes, mode = divmod(param_modes, 10)
				param_num = self.prog[pc+1+i]
				if mode == 0: # position
					param = Param(mode, self.prog[param_num], param_num)
				elif mode == 1: # immediate
					param = Param(mode, param_num)
				else:
					raise AssertionError(param_num)
				params.append(param)

			new_pc = None
			if op == Op.ADD:
				self.prog[params[2].pos] = params[0].val + params[1].val
			elif op == Op.MUL:
				self.prog[params[2].pos] = params[0].val * params[1].val
			elif op == Op.INP:
				val = self.input_queue.get()
				self.prog[params[0].pos] = val
			elif op == Op.OUT:
				self.output_queue.put(params[0].val)
			elif op == Op.JIT:
				if params[0].val != 0:
					new_pc = params[1].val
			elif op == Op.JIF:
				if params[0].val == 0:
					new_pc = params[1].val
			elif op == Op.ILT:
				self.prog[params[2].pos] = int(params[0].val < params[1].val)
			elif op == Op.IEQ:
				self.prog[params[2].pos] = int(params[0].val == params[1].val)
			else:
				raise AssertionError(op)

			if new_pc is None:
				pc += 1 + n_params
			else:
				pc = new_pc

if __name__ == '__main__':
	main()
