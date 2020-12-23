use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
	let lines: Vec<_> = read_lines("day3_input").collect();
	let nums = [
		count_trees(&lines, 1, 1),
		count_trees(&lines, 3, 1),
		count_trees(&lines, 5, 1),
		count_trees(&lines, 7, 1),
		count_trees(&lines, 1, 2),
	];
	println!("{:?} = {}", nums, nums.iter().fold(1, |prod: i64, &i| prod * i as i64));
}

fn count_trees(lines: &Vec<String>, right: usize, down: usize) -> i32 {
	let mut x_pos = 0;
	let mut y_pos = 0;
	let mut trees = 0;
	while y_pos < lines.len() {
		let line_bytes = lines[y_pos].as_bytes();
		let tile = line_bytes[x_pos % line_bytes.len()];
		if tile == b'#' {
			trees += 1;
		}

		x_pos += right;
		y_pos += down;
	}
	trees
}

fn read_lines(path: &str) -> impl Iterator<Item = String> {
	let path_p = Path::new(path);
	let file = match File::open(&path_p) {
		Err(why) => panic!("couldn't open {}: {}", path_p.display(), why),
		Ok(file) => file,
	};
	io::BufReader::new(file).lines().map(|line|
		match line {
			Err(why) => panic!("error reading line: {}", why),
			Ok(line) => line,
		}
	)
}
