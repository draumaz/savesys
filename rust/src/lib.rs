use std::fs::{File, OpenOptions};
use std::io::{prelude::*, Write, BufReader};
use std::path::Path;

pub fn str_reader(save_name: &'static str) -> Vec<String> {
    let file = File::open(save_name).expect("Couldn't open file for reading");
    return BufReader::new(file)
        .lines()
        .flatten()
        .flat_map(|line| line.parse::<String>())
        .collect();
}

pub fn str_writer(save_name: &'static str, line: usize, state: &str) {
    let mut read = str_reader(save_name);
    let mut file = OpenOptions::new().write(true).open(save_name).expect("Couldn't open file for writing");
    read[line] = state.to_string();
    for i in read {
        write!(file, "{}\n", i).expect("Couldn't write to file");
    }
}

pub fn str_generate(save_name: &'static str, save_size: i32) {
    let mut file = File::create(save_name).expect("Couldn't create file");
    for _ in 0..save_size {
        file.write(b"XXXXXXXXXXXX\n").expect("Couldn't write to file.");
    }
}

pub fn str_exists(save_name: &'static str) -> bool {
    return Path::new(save_name).exists();
}

pub fn i32_reader(save_name: &'static str) -> Vec<i32> {
    let file = File::open(save_name).expect("Couldn't open file for reading");
    return BufReader::new(file)
        .lines()
        .flatten()
        .flat_map(|line| line.parse::<i32>())
        .collect();
}

pub fn i32_writer(save_name: &'static str, line: usize, state: i32) {
    let mut read = i32_reader(save_name);
    let mut file = OpenOptions::new().write(true).open(save_name).expect("Couldn't open file for writing");
    read[line] = state;
    for i in read {
        write!(file, "{}\n", i).expect("Couldn't write to file");
    }
}

pub fn i32_generate(save_name: &'static str, save_size: i32) {
    let mut file = File::create(save_name).expect("Couldn't create file");
    for _ in 0..save_size {
        file.write(b"0\n").expect("Couldn't write to file");
    }
}

pub fn i32_exists(save_name: &'static str) -> bool {
    return Path::new(save_name).exists();
}
