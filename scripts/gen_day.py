import typer

from pathlib import Path

from bs4 import BeautifulSoup
from aocd.models import Puzzle
from jinja2 import Environment, FileSystemLoader

app = typer.Typer()

def get_puzzle_description(puzzle: Puzzle) -> str:
    """Get the puzzle description by parsing the prose HTML."""
    # Get the prose HTML
    prose = puzzle._get_prose()
    
    # Parse with BeautifulSoup
    soup = BeautifulSoup(prose, 'html.parser')
    
    # Find the article which contains the puzzle description
    article = soup.find('article')
    if article:
        # Extract text while preserving line breaks
        description = ""
        for element in article.children:
            if element.name == 'p':
                description += element.get_text() + "\n\n"
            elif element.name == 'pre':
                description += element.get_text() + "\n"
        return description.strip()
    return "Could not fetch puzzle description"

def get_solution_template(year: int, day: int) -> str:
    """Get the solution template from the jinja template file."""
    env = Environment(
        loader=FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("solution.py.jinja")

    solution_template = template.render(year=year, day=day)

    return solution_template


@app.command()
def generate(
    day: int = typer.Argument(..., help="Day to generate (0-25)"),
    year: int = typer.Argument(2024, help="Year of the event (default: 2024)"),
    ) -> None:
    """Generate the directory structure and files for a given AoC day"""
    if not 0 <= day <= 25:
        typer.echo(f"Day must be between 0 and 25, got {day}")
        raise typer.Exit(0)
    

    
    # Format day as two digits
    day_str = f"{day:02d}"

    # Create directory
    day_dir = Path(f"aoc/{day_str}")
    day_dir.mkdir(exist_ok=True)

    typer.echo(f"Generated files for day {day} ({day_dir}):")

    # Get puzzle data
    puzzle = Puzzle(year=year, day=day)
    
    # Save problem description
    problem_path = day_dir / "problem.txt"
    problem_path.write_text(get_puzzle_description(puzzle))
    typer.echo(f"  {problem_path}")

    # Save input
    input_path = day_dir / "input.txt"
    input_path.write_text(puzzle.input_data)

    typer.echo(f"  {input_path}")
    
    # Create solution file
    solution_path = day_dir / "solution.py"
    if not solution_path.exists():  # Don't overwrite existing solution
        solution_template = get_solution_template(year, day)
        solution_path.write_text(solution_template, encoding="utf-8")
        typer.echo(f"  {solution_path}")

if __name__ == "__main__":
    app()