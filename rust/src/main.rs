extern crate savesys;

use savesys::*;

fn main() {
    if exists("data.txt") == false { // Check/generate file (20 is the length of the file)
        generate("data.txt", 20); 
    }
    let mut save: Vec<i32> = savesys::reader("data.txt"); // Store reader vector in i
    
    println!("- Line two: {}\n- calling save_writer(2, 7)", save[2]);

    writer("data.txt", 2, 7); // Write variable 7 to line 2

    save = reader("data.txt"); // Recall

    println!("- Line two: {}", save[2]);
}
