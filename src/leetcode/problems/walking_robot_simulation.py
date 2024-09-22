import click

from ..command import get_problem_name
from ..judge import simple_judge
from ..test_cases import filter_and_zip


TEST_CASES = [
    [[4, -1, 3], []],
    [[4, -1, 4, -2, 4], [[2, 4]]],
    [[6, -1, -1, 6], []],
]

EXPECTED = [
    25,
    65,
    36,
]


@click.command(get_problem_name(__file__))
@click.argument("test-cases", nargs=-1, type=click.IntRange(0, len(TEST_CASES) - 1))
def problem(test_cases: list[int]):
    for case, expected in filter_and_zip(TEST_CASES, EXPECTED, test_cases):
        print(f"{case=}", end=" ")
        actual = solution(*case)
        correct = simple_judge(actual, expected)
        print(f"{correct=} {expected=} {actual=}")


def solution(commands: list[int], obstacles: list[list[int]]) -> int:
    obs = set(map(tuple, obstacles))

    curr_dir = (0, 1)
    curr_pos = (0, 0)
    max_dist = 0

    for command in commands:
        if command == -1:
            curr_dir = (curr_dir[1], -curr_dir[0])
        elif command == -2:
            curr_dir = (-curr_dir[1], curr_dir[0])
        else:
            for _ in range(command):
                new_pos = (
                    curr_pos[0] + curr_dir[0],
                    curr_pos[1] + curr_dir[1],
                )

                if new_pos not in obs:
                    curr_pos = new_pos
                else:
                    break

            max_dist = max(max_dist, curr_pos[0] ** 2 + curr_pos[1] ** 2)

    return max_dist
