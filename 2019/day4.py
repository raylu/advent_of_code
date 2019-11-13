#!/usr/bin/env python3

def main():
	valid_count = 0
	for password in range(146810, 612564+1):
		digits = tuple(map(int, str(password)))

		no_desc = True
		adj_same_exactly_2 = False
		adj_same = 1
		prev = digits[0]
		for digit in digits[1:]:
			if digit < prev:
				no_desc = False
				break
			if not adj_same_exactly_2:
				if digit == prev:
					adj_same += 1
				else:
					if adj_same == 2:
						adj_same_exactly_2 = True
					adj_same = 1
			prev = digit
		if not no_desc:
			continue
		if not adj_same_exactly_2 and adj_same == 2:
			adj_same_exactly_2 = True

		if adj_same_exactly_2:
			valid_count += 1
	print(valid_count)

if __name__ == '__main__':
	main()
