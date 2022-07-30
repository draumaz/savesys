extern crate savesys;
use savesys::*;

fn main() {
    if exists("data.txt") == false { generate("data.txt", 20) };

    let save_vec: Vec<i32> = savesys::reader("data.txt");
    
    if save_vec[5] != 7 { writer("data.txt", 5, 7) }
}
