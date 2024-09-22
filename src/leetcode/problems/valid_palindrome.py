import click

from ..command import get_problem_name
from ..judge import simple_judge
from ..test_cases import filter_and_zip


TEST_CASES = [
    ["A man, a plan, a canal: Panama"],
    ["race a car"],
    [" "],
]

EXPECTED = [
    True,
    False,
    True,
]


@click.command(get_problem_name(__file__))
@click.argument("test-cases", nargs=-1, type=click.IntRange(0, len(TEST_CASES) - 1))
def problem(test_cases: list[int]):
    for case, expected in filter_and_zip(TEST_CASES, EXPECTED, test_cases):
        actual = solution3(*case)
        correct = simple_judge(actual, expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return all(c == r for c, r in zip(cleaned, reversed(cleaned)))


def solution2(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    length = len(cleaned)

    for i in range(0, length // 2):
        if cleaned[i] != cleaned[length - i - 1]:
            return False

    return True


def solution3(s: str) -> bool:
    start = 0
    end = len(s) - 1

    while True:
        if start >= end:
            return True
        elif not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
