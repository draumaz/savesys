extern crate savesys;
use savesys::{reader, writer, exists};

fn main() {
    savesys::exists("data.txt", 20); // Generate/check file (20 is the length of the file)

    let mut i: <Vec:i32> = savesys::reader("data.txt"); // Store reader vector in i
    println!("- Line two: {}\n- calling save_writer(2, 7)", i[2]);

    savesys::writer("data.txt", 2, 7); // Write variable 7 to line 2

    i = savesys::reader("data.txt"); // Recall

    println!("- Line two: {}", i[2]);
}
