use std::fs::File;
use std::io::Write;
use std::path::Path;

// BEGIN CONFIG //

static SAVE_NAME: &'static str = "data.txt";
static SAVE_SIZE: i32          = 20;

// END CONFIG //

fn save_generate() {
    let mut file = File::create(SAVE_NAME).unwrap();
    for _ in 0..SAVE_SIZE {
        file.write(b"0\n").unwrap();
    }
}

fn save_exists() {
    if Path::new(SAVE_NAME).exists() == false {
        save_generate();
    } else {
        println!("File already exists");
    }
}

fn main() {
    save_exists();
}
