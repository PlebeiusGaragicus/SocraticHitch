# Socratic Hitch

This project is meant to help users collect their thoughts into cogent "Socratic" arguments in an effort to enable their arguments to be as rich and hard-hitting as those of the beloved Christopher Hitchens.

## Getting Started

To get started with Socratic Hitch, simply clone the repository and run the compilation script:

```bash
git clone https://github.com/your-username/SocraticHitch.git
cd SocraticHitch
./compile.sh
```

The `./compile.sh` script will:
1.  Automatically create a Python virtual environment (`venv`) if it doesn't exist.
2.  Install the necessary dependencies from `requirements.txt`.
3.  Compile the Markdown files located in `docs/example-arguments/` into HTML.
4.  Output the compiled HTML files into the `compiled-html/` folder at the project root.

## Usage

You can also compile specific files or use light mode:

```bash
# Show help and usage options
./compile.sh --help

# Compile using light mode instead of the default dark mode
./compile.sh --light

# Compile a specific markdown file
./compile.sh path/to/your/argument.md
```


---
