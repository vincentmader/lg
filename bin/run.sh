#!/bin/sh

a="$0"
b="$(realpath $a)"
c="$(dirname $b)"

# Define path to python executable (in virtual environment).
  PYTHON3="$c/../.venv/bin/python3"

# Execute main python entrypoint.
  cd "$c/../src" && $PYTHON3 ./main.py
