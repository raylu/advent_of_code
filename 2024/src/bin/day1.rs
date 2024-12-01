use aoc2024::read_lines;

fn main() {
    let mut l1 = vec![];
    let mut l2 = vec![];
    for line in read_lines("day1.txt") {
        let (first, second) = line.split_once("   ").unwrap();
        l1.push(first.parse::<i32>().unwrap());
        l2.push(second.parse::<i32>().unwrap());
    }
    l1.sort_unstable();
    l2.sort_unstable();
    let total_distance = l1.into_iter().zip(l2.into_iter()).map(|it| {
        let (first, second) = it;
        (first - second).abs()
    }).sum::<i32>();
    println!("total distance: {}", total_distance);
}
