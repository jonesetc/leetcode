import click

from .problem_template import problem_template
from .problem_2022 import problem_2022
from .problem_1894 import problem_1894
from .problem_1945 import problem_1945
from .problem_874 import problem_874


@click.group(help="Tool for running some leetcode stuff")
def cli() -> str:
    pass


cli.add_command(problem_template)
cli.add_command(problem_2022)
cli.add_command(problem_1894)
cli.add_command(problem_1945)
cli.add_command(problem_874)

if __name__ == "__main__":
    cli()
