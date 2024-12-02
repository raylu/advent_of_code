use aoc2024::read_lines;

fn main() {
    let safe = read_lines("day2.txt")
        .map(|line| {
            let report: Vec<i32> = line.split(' ').map(|x| x.parse::<i32>().unwrap()).collect();
            if is_safe(&report) {
                1
            } else {
                for i in 0..report.len() {
                    let dampened = report[0..i]
                        .iter()
                        .cloned()
                        .chain(report[i + 1..].iter().cloned())
                        .collect();
                    if is_safe(&dampened) {
                        return 1;
                    }
                }
                0
            }
        })
        .sum::<i32>();
    println!("safe: {}", safe);
}

fn is_safe(report: &Vec<i32>) -> bool {
    // adjacent levels >= 1 and <= 3
    if !AdjacentPairs::new(report).all(|(prev, cur)| {
        let diff = cur.abs_diff(prev);
        diff >= 1 && diff <= 3
    }) {
        return false;
    }
    // all increasing/decreasing
    return AdjacentPairs::new(report).all(|(prev, cur)| cur > prev)
        || AdjacentPairs::new(report).all(|(prev, cur)| cur < prev);
}

struct AdjacentPairs<'a, T> {
    vector: &'a Vec<T>,
    index: usize,
}
impl<'a, T> AdjacentPairs<'a, T> {
    fn new(vector: &'a Vec<T>) -> Self {
        Self { vector, index: 1 }
    }
}
impl<'a, T> Iterator for AdjacentPairs<'a, T>
where
    T: Copy,
{
    type Item = (T, T);

    fn next(&mut self) -> Option<Self::Item> {
        if self.index == self.vector.len() {
            None
        } else {
            let pair = Some((self.vector[self.index - 1], self.vector[self.index]));
            self.index += 1;
            pair
        }
    }

    fn size_hint(&self) -> (usize, Option<usize>) {
        let remaining = self.vector.len() - self.index;
        (remaining, Some(remaining))
    }
}
