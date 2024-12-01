use std::{fs::File, io::{self, BufRead}, path::Path};

pub fn read_lines(path: &str) -> impl Iterator<Item = String> {
    let file = File::open(Path::new(path)).unwrap();
    io::BufReader::new(file).lines().map(|line| line.unwrap())
}
