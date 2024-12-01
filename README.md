# Advent of Code 2024

Solutions for [Advent of Code 2024](https://adventofcode.com/2024) using Python.

## Setup

### Prerequisites
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for package management
- Your Advent of Code session token

### Getting Your Session Token
1. Go to [Advent of Code](https://adventofcode.com/2024) and log in
2. Open your browser's developer tools (usually F12)
3. Go to the Application/Storage tab
4. Find the cookie named `session`
5. Copy its value

### Installation

1. Create a directory for your session token:
```bash
mkdir -p ~/.config/aocd
```

2. Save your session token:
```bash
echo "your_session_token_here" > ~/.config/aocd/token
```

3. Install dependencies:
If you are using `uv`, simply using `uv run <script>` will install dependencies automatically, but to manually install:
```bash
uv sync
```

## Usage

### Generating a New Day
To set up the files for a new day:
```bash
uv run scripts/gen_day.py <day>
```

For example, to generate day 1:
```bash
uv run scripts/gen_day.py 1
```

This will create:
- `aoc/<day>/solution.py` - Template for your solution
- `aoc/<day>/input.txt` - Your puzzle input
- `aoc/<day>/problem.txt` - The puzzle description

### Working on Solutions
1. Edit `solution.py` with your solution in the `part1` and `part2` functions

2. Run your solution:
```bash
uv run aoc/01/solution.py
```

### Features
The solution template includes:
- Automatic testing against example data
- Visual feedback on test results
- Automatic submission of correct answers from the example data
- Part 2 remains locked until Part 1 is solved
- Progress indicators and colorized output

### Project Structure
```
advent-of-code-2024/
├── aoc/
│   └── 01/                # One directory per day
│       ├── solution.py    # Your solution code
│       ├── input.txt      # Your puzzle input
│       └── problem.txt    # Puzzle description
├── scripts/
│   └── gen_day.py        # Day generator script
├── templates/
│   └── solution.py.jinja # Solution template
└── pyproject.toml        # Project dependencies
```

## Tips
- Each day's `solution.py` automatically tests against example data from the puzzle
- Test results show expected vs actual output for debugging when running the examples
- Part 2 is automatically unlocked after completing Part 1
- Solutions are automatically submitted when tests pass

## Contributing
Feel free to submit issues or pull requests with improvements!

## License
[MIT License](LICENSE)