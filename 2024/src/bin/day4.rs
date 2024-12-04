use aoc2024::read_lines;

fn main() {
	let word_search: Vec<Vec<u8>> = read_lines("day4.txt").map(|line| line.as_bytes().to_vec()).collect();
	let mut xmas = 0;
	for (y, row) in word_search.iter().enumerate() {
		for (x, ch) in row.iter().enumerate() {
			if *ch == b'A' && is_xmas(&word_search, y.try_into().unwrap(), x.try_into().unwrap()) {
				println!("at {}, {}", y, x);
				xmas += 1;
			}
		}
	}
	println!("xmas: {}", xmas);
}

fn is_xmas(word_search: &[Vec<u8>], y: i32, x: i32) -> bool {
	let delta1: [(i8, i8); 2] = [(-1, -1), (1, 1)];
	let delta2: [(i8, i8); 2] = [(-1, 1), (1, -1)];
	let word1 = get_word(word_search, y, x, &delta1);
	let word2 = get_word(word_search, y, x, &delta2);
	(word1 == [b'M', b'S'] || word1 == [b'S', b'M']) && (word2 == [b'M', b'S'] || word2 == [b'S', b'M'])
}

fn get_word(word_search: &[Vec<u8>], y: i32, x: i32, deltas: &[(i8, i8)]) -> [u8; 2] {
	let mut word: [u8; 2] = [0; 2];
	for (i, (dy, dx)) in deltas.iter().enumerate() {
		let y: i32 = y + i32::from(*dy);
		let x: i32 = x + i32::from(*dx);
		if y < 0 || y >= word_search.len().try_into().unwrap() || x < 0 || x >= word_search[0].len().try_into().unwrap()
		{
			break;
		}
		word[i] = word_search[usize::try_from(y).unwrap()][usize::try_from(x).unwrap()];
	}
	word
}
