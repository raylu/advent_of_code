use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

#[derive(Debug)]
struct Line {
	low: i32,
	high: i32,
	letter: char,
	password: String,
}

fn main() {
	let lines = read_lines("day2_input");
	let line_structs = lines.map(|line| {
		let mut split = line.splitn(2, ": ");
		let rule = split.next().unwrap();
		let password = split.next().unwrap().to_string();

		let mut rule_split = rule.splitn(2, ' ');
		let range = rule_split.next().unwrap();
		let letter: char = rule_split.next().unwrap().parse().unwrap();

		rule_split = range.splitn(2, '-');
		let low: i32 = rule_split.next().unwrap().parse().unwrap();
		let high: i32 = rule_split.next().unwrap().parse().unwrap();

		Line{low: low, high: high, letter: letter, password: password}
	});

	let mut valid = 0;
	for line in line_structs {
		let mut count = 0;
		for c in line.password.chars() {
			if c == line.letter {
				count += 1;
				if count > line.high {
					break;
				}
			}
		}
		if line.low <= count && count <= line.high {
			valid += 1;
		}
	}
	println!("{}", valid);
}

fn read_lines(path: &str) -> impl Iterator<Item = String> {
	let path_p = Path::new(path);
	let file = match File::open(&path_p) {
		Err(why) => panic!("couldn't open {}: {}", path_p.display(), why),
		Ok(file) => file,
	};
	let lines = io::BufReader::new(file).lines().map(|line|
		match line {
			Err(why) => panic!("error reading line: {}", why),
			Ok(line) => line,
		}
	);
	lines
}
