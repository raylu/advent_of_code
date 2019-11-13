#!/usr/bin/env python3

import copy
import enum
import fileinput

def main():
	with fileinput.input() as f:
		prog = list(map(int, next(f).split(',')))
	run(prog)

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

def run(prog):
	pc = 0
	while prog[pc] != 99:
		opcode = prog[pc]
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
			param_num = prog[pc+1+i]
			if mode == 0: # position
				param = Param(mode, prog[param_num], param_num)
			elif mode == 1: # immediate
				param = Param(mode, param_num)
			else:
				raise AssertionError(param_num)
			params.append(param)

		new_pc = None
		if op == Op.ADD:
			prog[params[2].pos] = params[0].val + params[1].val
		elif op == Op.MUL:
			prog[params[2].pos] = params[0].val * params[1].val
		elif op == Op.INP:
			prog[params[0].pos] = int(input('input: '))
		elif op == Op.OUT:
			print(params[0].val)
		elif op == Op.JIT:
			if params[0].val != 0:
				new_pc = params[1].val
		elif op == Op.JIF:
			if params[0].val == 0:
				new_pc = params[1].val
		elif op == Op.ILT:
			prog[params[2].pos] = int(params[0].val < params[1].val)
		elif op == Op.IEQ:
			prog[params[2].pos] = int(params[0].val == params[1].val)
		else:
			raise AssertionError(op)

		if new_pc is None:
			pc += 1 + n_params
		else:
			pc = new_pc

if __name__ == '__main__':
	main()
