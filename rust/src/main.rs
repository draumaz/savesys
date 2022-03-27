mod savesys;

fn main() {
    savesys::exists();
    let mut i = savesys::reader();
    println!("- Line two: {}\n- calling save_writer(2, 7)", i[2]);
    savesys::writer(2, 7);
    i = savesys::reader();
    println!("- Line two: {}", i[2]);
}
