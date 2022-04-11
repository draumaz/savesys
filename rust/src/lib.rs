use std::fs::{File, OpenOptions};
use std::io::{prelude::*, Write, BufReader};
use std::path::Path;

pub fn reader(save_name: &'static str) -> Vec<i32> {
    let file = File::open(save_name).expect("Couldn't open file for reading");
    return BufReader::new(file)
        .lines()
        .flatten()
        .flat_map(|line| line.parse::<i32>())
        .collect();
}

pub fn writer(save_name: &'static str, line: usize, state: i32) {
    let mut read = reader(save_name);
    let mut file = OpenOptions::new().write(true).open(save_name).expect("Couldn't open file for writing");
    read[line] = state;
    for i in read {
        write!(file, "{}\n", i).expect("Couldn't write to file.");
    }
}

pub fn generate(save_name: &'static str, save_size: i32) {
    let mut file = File::create(save_name).expect("Couldn't create file");
    for _ in 0..save_size {
        file.write(b"0\n").expect("Couldn't write to file");
    }
}

pub fn exists(save_name: &'static str) -> bool {
    return Path::new(save_name).exists() == false;
}
