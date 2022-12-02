use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let mut file = File::open("in.txt").unwrap();
    let mut lines = BufReader::new(file).lines();
    let mut totals = vec![];
    let mut total = 0;
    for line in lines {
        match line.unwrap().as_str() {
            "" => {
                totals.push(total);
                total = 0;
            },
            num => {
                let shit: i32 = num.parse().unwrap();
                total += shit;
            }
        }
    }
    println!("{:?}", totals.iter().max());
}