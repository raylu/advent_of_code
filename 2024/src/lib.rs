use std::{
	fs::File,
	io::{self, BufRead, Read},
	path::Path,
};

pub fn read_lines(path: &str) -> impl Iterator<Item = String> {
	let file = File::open(Path::new(path)).unwrap();
	io::BufReader::new(file).lines().map(|line| line.unwrap())
}

pub fn read_file(path: &str) -> String {
	let mut file = File::open(Path::new(path)).unwrap();
	let mut contents = String::new();
	file.read_to_string(&mut contents).unwrap();
	contents
}
