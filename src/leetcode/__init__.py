import click

from .problem_2022 import problem_2022
from .problem_1894 import problem_1894


@click.group(help="Tool for running some leetcode stuff")
def cli() -> str:
    pass


cli.add_command(problem_2022)
cli.add_command(problem_1894)

if __name__ == "__main__":
    cli()
