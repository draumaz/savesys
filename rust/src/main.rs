use std::fs::File;
use std::io::{prelude::*, Write, BufReader};
use std::path::Path;

// BEGIN CONFIG //

static SAVE_NAME: &'static str = "data.txt";
static SAVE_SIZE: i32          = 20;

// END CONFIG //

fn save_reader() -> Vec<i32> {
    let file = File::open(SAVE_NAME).unwrap();
    let v: Vec<i32> = BufReader::new(file)
        .lines()
        .flatten()
        .flat_map(|line| line.parse::<i32>())
        .collect();
    return v;
}

fn save_generate() {
    let mut file = File::create(SAVE_NAME).unwrap();
    for i in 0..SAVE_SIZE {
        file.write(b"0\n").unwrap();
    }
}

fn save_exists() {
    if Path::new(SAVE_NAME).exists() == false {
        save_generate();
    }
}

fn main() {
    save_exists();
    let i = save_reader();
    println!("{}", i[2]);
}
