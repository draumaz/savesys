use std::fs::{File, OpenOptions};
use std::io::{prelude::*, Write, BufReader};
use std::path::Path;

// BEGIN CONFIG //

static SAVE_NAME: &'static str = "data.txt";
static SAVE_SIZE: i32          = 20;

// END CONFIG //

pub fn reader() -> Vec<i32> {
    let file = File::open(SAVE_NAME).expect("Couldn't open file for reading");
    return BufReader::new(file)
        .lines()
        .flatten()
        .flat_map(|line| line.parse::<i32>())
        .collect();
}

pub fn writer(line: usize, state: i32) {
    let mut read = reader();
    let mut file = OpenOptions::new().write(true).open(SAVE_NAME).expect("Couldn't open file for writing");
    read[line] = state;
    for i in read {
        write!(file, "{}\n", i).expect("Couldn't write to file.");
    }
}

pub fn generate() {
    let mut file = File::create(SAVE_NAME).expect("Couldn't create file");
    for _ in 0..SAVE_SIZE {
        file.write(b"0\n").expect("Couldn't write to file");
    }
}

pub fn exists() {
    if Path::new(SAVE_NAME).exists() == false {
        generate();
    }
}
