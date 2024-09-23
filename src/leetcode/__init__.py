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
def cli():
    pass


@cli.command("list", help="Run a problem by name")
def list_problems():
    print("Available problems:")
    for p in get_problems():
        print(f"  {p.replace("_", "-")}")


@cli.group(help="Run a problem by name")
def run():
    pass


@cli.group("open", help="Open a problem by name")
def open_problem():
    pass


for problem in get_problems():
    module = import_module(f"leetcode.problems.{problem}")
    run.add_command(module.Problem.run_test_cases)
    open_problem.add_command(module.Problem.open_problem)


if __name__ == "__main__":
    cli()
