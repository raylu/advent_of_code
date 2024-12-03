use aoc2024::read_file;

fn main() {
	let instr = read_file("day3.txt");
	let mut instr = instr.as_str();
	let mut sum = 0;
	while let Some((index, product)) = parse(instr) {
		sum += product.unwrap_or_default();
		instr = &instr[index..];
	}
	println!("{}", sum);
}

fn parse(instr: &str) -> Option<(usize, Option<i32>)> {
	print!("{}", instr);
	let start = instr.find("mul(")?;
	let instr = &instr[start + 4..];
	let end = instr.find(')')?;
	if let Some((op1, op2)) = instr[..end].split_once(',') {
		if let Ok(product) = op1.parse::<i32>().and_then(|op1| op2.parse::<i32>().map(|op2| op1 * op2)) {
			println!("\t{:?}", product);
			return Some((start + 4 + end + 1, Some(product)));
		}
	}
	Some((start + 4, None))
}
