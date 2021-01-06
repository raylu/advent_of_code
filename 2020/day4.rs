use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
	let expected: HashSet<String> = vec![
		"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt",
	].into_iter().map(|s| s.to_string()).collect();
	let lines = read_lines("day4_input");

	let mut valid = 0;
	let mut fields: HashSet<String> = HashSet::new();
	for line in lines {
		if line == "" {
			if valid_batch(&expected, &fields) {
				valid += 1;
			}
			fields.clear();
		} else {
			for field in line.split(' ') {
				let name = field.splitn(2, ':').next().unwrap();
				fields.insert(name.to_string());
			}
		}
	}
	if valid_batch(&expected, &fields) {
		valid += 1;
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

fn valid_batch(expected: &HashSet<String>, fields: &HashSet<String>) -> bool {
	return expected.difference(fields).next().is_none();
}
