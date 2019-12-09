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

	input_queue = queue.Queue(1)
	output_queue = queue.Queue(1)
	input_queue.put_nowait(int(input('mode: ')))
	program = Program(copy.copy(original_prog), input_queue, output_queue)
	thread = threading.Thread(target=program.run)
	thread.start()
	while thread.is_alive():
		print(program.output_queue.get())
	print(program.output_queue.get_nowait())

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
	ARB = 9

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
		pc = rel_base = 0
		while self.prog[pc] != 99:
			opcode = self.prog[pc]
			param_modes, op = divmod(opcode, 100)
			op = Op(op)

			if op in (Op.ADD, Op.MUL, Op.ILT, Op.IEQ):
				n_params = 3
			elif op in (Op.INP, Op.OUT, Op.ARB):
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
					self.allocate(param_num)
					param = Param(mode, self.prog[param_num], param_num)
				elif mode == 1: # immediate
					param = Param(mode, param_num)
				elif mode == 2: # relative
					pos = rel_base + param_num
					self.allocate(pos)
					param = Param(mode, self.prog[pos], pos)
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
			elif op == Op.ARB:
				rel_base += params[0].val
			else:
				raise AssertionError(op)

			if new_pc is None:
				pc += 1 + n_params
			else:
				pc = new_pc

	def allocate(self, pos):
		if pos < 0:
			raise ValueError(pos)
		if pos >= len(self.prog):
			self.prog.extend(0 for _ in range(pos - len(self.prog) + 1))

if __name__ == '__main__':
	main()
