use aoc2024::read_file;

fn main() {
	let instructions = read_file("day3.txt");
	let mut instructions = instructions.as_str();
	let mut mul_enabled = true;
	let mut sum = 0;
	while let Some((index, instr)) = parse(instructions) {
		match instr {
			Some(Instr::Mul(product)) => {
				if mul_enabled {
					sum += product;
				}
			},
			Some(Instr::Do) => mul_enabled = true,
			Some(Instr::Dont) => mul_enabled = false,
			None => {},
		}
		instructions = &instructions[index..];
	}
	println!("{}", sum);
}

enum Instr {
	Mul(i32),
	Do,
	Dont,
}

fn parse(instr: &str) -> Option<(usize, Option<Instr>)> {
	print!("{}", instr);
	let mul_start = instr.find("mul(");
	let do_start = instr.find("do()");
	let dont_start = instr.find("don't()");
	let min = mul_start
		.unwrap_or(usize::MAX)
		.min(do_start.unwrap_or(usize::MAX))
		.min(dont_start.unwrap_or(usize::MAX));

	if mul_start.is_some() && min == mul_start.unwrap() {
		let start = mul_start.unwrap();
		let instr = &instr[start + 4..];
		let end = instr.find(')')?;
		if let Some((op1, op2)) = instr[..end].split_once(',') {
			if let Ok(product) = op1.parse::<i32>().and_then(|op1| op2.parse::<i32>().map(|op2| op1 * op2)) {
				println!("\t{:?}", product);
				return Some((start + 4 + end + 1, Some(Instr::Mul(product))));
			}
		}
		Some((start + 4, None))
	} else if do_start.is_some() && min == do_start.unwrap() {
		let start = do_start.unwrap();
		Some((start + 4, Some(Instr::Do)))
	} else if dont_start.is_some() && min == dont_start.unwrap() {
		let start = dont_start.unwrap();
		Some((start + 7, Some(Instr::Dont)))
	} else {
		None
	}
}
