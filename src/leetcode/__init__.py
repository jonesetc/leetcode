from pathlib import Path
from importlib import import_module

import click


problems_path = Path(__file__).resolve().parent / "problems"
problems = [
    file.name.removesuffix(".py")
    for file in problems_path.glob("*.py")
    if file.is_file()
    and file.name != "__init__.py"
    and file.name != "problem_template.py"
]


@click.group(help="Tool for running some leetcode stuff")
def cli() -> str:
    pass


for problem in problems:
    module = import_module(f".problems.{problem}", "leetcode")
    cli.add_command(module.problem)

if __name__ == "__main__":
    cli()
