// build.rs
// following https://github.com/tchernobog/rfcs/blob/master/text/0000-cargo-run-deps.md
use std::{env, process::Command};

fn main() {
    let cargo_path = env::var("CARGO").unwrap();
    let mut mdbook = Command::new(cargo_path).args(&[
        "run",
        "--package",
        "mdbook",
        "--",
        "build",
    ]);

}