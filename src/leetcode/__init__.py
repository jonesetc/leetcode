from pathlib import Path
from importlib import import_module

import click


def get_problems() -> list[str]:
    return [
        file.name.removesuffix(".py")
        for file in (Path(__file__).resolve().parent / "problems").glob("*.py")
        if file.is_file() and file.name != "__init__.py"
    ]


@click.group(help="Tool for running some leetcode stuff")
def cli() -> str:
    pass


for problem in get_problems():
    module = import_module(f"leetcode.problems.{problem}")
    cli.add_command(module.problem)

if __name__ == "__main__":
    cli()
