use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
	let lines = read_lines("day3_input");
	let mut x_pos = 0;
	let mut trees = 0;
	for line in lines {
		let line_bytes = line.as_bytes();
		let tile = line_bytes[x_pos % line_bytes.len()];
		println!("{} {}:\t{}", line, x_pos, tile as char);
		if tile == b'#' {
			trees += 1;
		}
		x_pos += 3;
	}
	println!("{}", trees);
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
