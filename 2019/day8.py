#!/usr/bin/env python3

import fileinput

def main():
	for line in fileinput.input():
		image_data = line.rstrip()
		break

	width = 25
	height = 6
	layer_size = width * height
	image = [[' '] * width for _ in range(height)]

	min_zeroes = float('inf')
	for layer_offset in range(0, len(image_data), layer_size):
		layer = image_data[layer_offset:layer_offset + layer_size]
		for row, row_offset in enumerate(range(0, layer_size, width)):
			row_pixels = layer[row_offset:row_offset+width]
			for col, pixel in enumerate(row_pixels):
				if pixel != '2' and image[row][col] == ' ':
					image[row][col] = pixel
	for row_pixels in image:
		for pixel in row_pixels:
			if pixel == '1':
				print('W', end='')
			else:
				print(' ', end='')
		print()

if __name__ == '__main__':
	main()
