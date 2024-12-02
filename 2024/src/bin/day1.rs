use std::collections::HashMap;

use aoc2024::read_lines;

fn main() {
	let mut l1: Vec<i32> = vec![];
	let mut l2: HashMap<i32, i32> = HashMap::with_capacity(1000);
	for line in read_lines("day1.txt") {
		let (left, right) = line.split_once("   ").unwrap();
		l1.push(left.parse::<i32>().unwrap());
		let right = right.parse::<i32>().unwrap();
		match l2.get_mut(&right) {
			Some(freq) => {
				*freq += 1;
			},
			None => {
				l2.insert(right, 1);
			},
		}
	}
	let similarity = l1
		.into_iter()
		.map(|left| {
			let freq = l2.get(&left).map_or(0, |freq| *freq);
			left * freq
		})
		.sum::<i32>();
	println!("similarity: {}", similarity);
}
