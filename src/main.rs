// dummy file

use mdbook::MDBook;

fn main() {
	let root_dir = "./";
	let mut md = MDBook::load(root_dir)
    	.expect("Unable to load the book");
	md.build().expect("Building failed");



	// println!("This package does nothing! It's just for gathering deps to build the book!")


}