extern crate savesys;

use savesys::*;

fn main() {
    if i32_exists("data.txt") == false { // Check/generate file (20 is the length of the file)
        i32_generate("data.txt", 20); 
    }
    
    let mut save: Vec<i32> = savesys::i32_reader("data.txt"); // Store reader vector in i
    
    println!("- Line two: {}\n- calling i32_writer", save[2]);
    
    i32_writer("data.txt", 2, 7); // Write variable 7 to line 2

    save = i32_reader("data.txt"); // Recall

    println!("- Line two: {}", save[2]);

    // Below is the same thing, but for fetching Strings.

    if str_exists("data2.txt") == false {
        str_generate("data2.txt", 20);
    }

    let mut save2: Vec<String> = str_reader("data2.txt");

    println!("- Line two: {}\n- calling str_writer", save2[2]);

    str_writer("data2.txt", 2, "Hello, world!");

    save2 = str_reader("data2.txt");

    println!("- Line two: {}", save2[2]);
}
