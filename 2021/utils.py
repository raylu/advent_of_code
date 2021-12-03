def iter_lines(day):
	with open(f'day{day}_input', 'r', encoding='ascii') as f:
		for line in f:
			yield line.rstrip('\n')
