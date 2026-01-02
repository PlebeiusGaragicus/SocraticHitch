#!/bin/bash

# Usage help
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Usage: ./compile.sh [--light] [path_to_markdown_file]"
    echo "Description: Activates the virtual environment and compiles Socratic Seminar markdown files to HTML."
    echo "If no file path is provided, it compiles all .md files in docs/example-arguments/ to scripts/compiled-html/"
    echo "Options:"
    echo "  --light    Default to light mode instead of dark mode."
    exit 0
fi

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Check if venv exists
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "Error: Virtual environment 'venv' not found in $SCRIPT_DIR."
    echo "Please create it first with: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate the virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Call the python script with the provided arguments
python3 "$SCRIPT_DIR/compile_socratic.py" "$@"

# Deactivate the virtual environment
deactivate
