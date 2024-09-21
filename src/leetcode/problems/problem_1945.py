import click

from ..judge import simple_judge
from ..test_cases import filter_and_zip


TEST_CASES = [["iiii", 1], ["leetcode", 2], ["zbax", 2], ["dbvmfhnttvr", 5]]

EXPECTED = [
    36,
    6,
    8,
    5,
]


@click.command("1945")
@click.argument("test-cases", nargs=-1, type=click.IntRange(0, len(TEST_CASES) - 1))
def problem(test_cases: list[int]):
    for case, expected in filter_and_zip(TEST_CASES, EXPECTED, test_cases):
        actual = solution(*case)
        correct = simple_judge(actual, expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(s: str, k: int) -> int:
    s = "".join(map(lambda x: str(ord(x) - 96), s))
    while k and len(s) > 1:
        s = sum(map(lambda x: int(x), s))
        if k := k - 1:
            s = str(s)
    return int(s)
