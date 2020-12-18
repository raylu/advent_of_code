use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
	let nums = read_lines("day1_input");
	let target = 2020;
	let mut complements: HashMap<i32, i32> = HashMap::new();
	for (i, num1) in nums.iter().enumerate() {
		for j in i+1..nums.len() {
			let num2 = nums[j];
			let sum = num1 + num2;
			let complement = target - sum;
			complements.insert(complement, *num1);
		}
	}
	for num in nums {
		if let Some(&num1) = complements.get(&num) {
			println!("{} + {} + {}", num, num1, target - num - num1);
		}
	}
}

fn read_lines(path: &str) -> Vec<i32> {
	let path_p = Path::new(path);
	let file = match File::open(&path_p) {
		Err(why) => panic!("couldn't open {}: {}", path_p.display(), why),
		Ok(file) => file,
	};
	let lines = io::BufReader::new(file).lines();

	let mut numbers: Vec<i32> = vec![];
	for line in lines {
		match line {
			Err(why) => panic!("error reading line: {}", why),
			Ok(line) => numbers.push(line.parse().unwrap()),
		}
	}
	numbers
}
