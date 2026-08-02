# Puzzle Solver

A Python program that finds the longest possible one-dimensional numeric puzzle chain, where two adjacent fragments are connected by matching the last two digits of the previous fragment with the first two digits of the next fragment.

## Requirements

- Python 3.12 or newer
- uv

## Installation

If you do not have **uv** installed, install it with:

```bash
pip install uv
```

## Usage

Run the program by specifying the input file:

```bash
uv run main.py source.txt
```

or

```bash
uv run python main.py source.txt
```

You can replace `source.txt` with any text file that follows the required input format.

## Input Format

The input file must contain one numeric fragment per line.

Example:

```text
608017
248460
962282
994725
177092
```

## Output

The program prints:

- The longest numeric chain found.
- The total execution time.

## Notes

- Each fragment can be used **only once**.
- The program works with any valid input file that follows the required format.
- The solution uses only Python's standard library and does not require any external dependencies besides `uv` for execution.
