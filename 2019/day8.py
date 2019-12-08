#!/usr/bin/env python3

import fileinput

def main():
	for line in fileinput.input():
		image_data = line.rstrip()
		break

	width = 25
	height = 6
	layer_size = width * height

	min_zeroes = float('inf')
	for offset in range(0, len(image_data), layer_size):
		layer = image_data[offset:offset + layer_size]
		zeroes = layer.count('0')
		if zeroes < min_zeroes:
			min_zeroes = zeroes
			ans = layer.count('1') * layer.count('2')
	print(ans)

if __name__ == '__main__':
	main()
