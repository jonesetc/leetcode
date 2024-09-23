from pathlib import Path
from importlib import import_module

import click


def get_problems() -> list[str]:
    return [
        file.stem
        for file in (Path(__file__).resolve().parent / "problems").glob("*.py")
        if file.is_file()
        and file.name != "__init__.py"  # and file.name != "template.py"
    ]


@click.group(help="Tool for running some leetcode stuff")
def cli() -> str:
    pass


for problem in get_problems():
    module = import_module(f"leetcode.problems.{problem}")

    if hasattr(module, "Problem"):
        cli.add_command(module.Problem.run_test_cases)
    else:
        cli.add_command(module.problem)

if __name__ == "__main__":
    cli()
