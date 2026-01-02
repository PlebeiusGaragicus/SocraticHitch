# Socratic Hitch

see our [docs](https://plebeiusgaragicus.github.io/SocraticHitch/) for an explanation.

---

You can also compile specific files or use light mode:

```bash
# Show help and usage options
./compile --help

# Compile using light mode instead of the default dark mode
./compile --light

# Compile a specific markdown file
./compile path/to/your/argument.md
```

The `./compile.sh` script will:
1.  Automatically create a Python virtual environment (`venv`) if it doesn't exist.
2.  Install the necessary dependencies from `requirements.txt`.
3.  Compile the Markdown files located in `docs/example-arguments/` into HTML.
4.  Output the compiled HTML files into the `compiled-html/` folder at the project root.
