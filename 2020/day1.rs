use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
	let nums = read_lines("day1_input");
	let target = 2020;
	let mut complements: HashSet<i32> = vec![].into_iter().collect();
	for num in &nums {
		let complement = target - num;
		if complements.contains(num) {
			println!("{} + {} = {}", num, complement, target);
		}
		if !complements.insert(complement) {
			panic!("found {} twice", num);
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
