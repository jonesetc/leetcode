import click

from ..judge import simple_judge


TEST_CASES = [["iiii", 1], ["leetcode", 2], ["zbax", 2], ["dbvmfhnttvr", 5]]

EXPECTED = [
    36,
    6,
    8,
    5,
]


@click.command("1945")
def problem():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        actual = solution(*case)
        correct = simple_judge(actual, expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(s: str, k: int) -> int:
    s = ''.join(map(lambda x: str(ord(x) - 96), s))
    while k and len(s) > 1:
        s = sum(map(lambda x: int(x), s))
        if k := k - 1:
            s = str(s)
    return int(s)
