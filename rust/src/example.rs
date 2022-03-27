mod savesys;

fn main() {
    savesys::exists(); // Generate/check file

    let mut i = savesys::reader(); // Store reader vector in i
    println!("- Line two: {}\n- calling save_writer(2, 7)", i[2]);

    savesys::writer(2, 7); // Write variable 7 to line 2

    i = savesys::reader(); // Recall

    println!("- Line two: {}", i[2]);
}
