use aoc2024::read_lines;

fn main() {
	let word_search: Vec<Vec<u8>> = read_lines("day4.txt").map(|line| line.as_bytes().to_vec()).collect();
	let dirs: [(i8, i8); 8] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
	let mut xmas = 0;
	for (y, row) in word_search.iter().enumerate() {
		for (x, ch) in row.iter().enumerate() {
			if *ch == b'X' {
				xmas += dirs
					.iter()
					.filter(|dir| is_xmas(&word_search, y.try_into().unwrap(), x.try_into().unwrap(), **dir))
					.count();
			}
		}
	}
	println!("xmas: {}", xmas);
}

fn is_xmas(word_search: &Vec<Vec<u8>>, y: i32, x: i32, dir: (i8, i8)) -> bool {
	let mut word: [u8; 4] = [0; 4];
	for i in 0..4 {
		let y: i32 = y + (i32::try_from(i).unwrap() * i32::from(dir.0));
		let x: i32 = x + (i32::try_from(i).unwrap() * i32::from(dir.1));
		if y < 0 || y >= word_search.len().try_into().unwrap() || x < 0 || x >= word_search[0].len().try_into().unwrap()
		{
			return false;
		}
		word[i] = word_search[usize::try_from(y).unwrap()][usize::try_from(x).unwrap()];
	}
	word == [b'X', b'M', b'A', b'S']
}
