from itertools import accumulate
from bisect import bisect_right

from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[5, 1, 5], 22],
        [[3, 4, 1, 2], 25],
    ]

    EXPECTED = [
        0,
        1,
    ]

    @staticmethod
    def solution(chalk: list[int], k: int) -> int:
        remaining = k % sum(chalk)
        for i, curr in enumerate(chalk):
            remaining -= curr
            if remaining < 0:
                return i

    @staticmethod
    def solution2(chalk: list[int], k: int) -> int:
        remaining = k % sum(chalk)
        for i, curr in enumerate(accumulate(chalk)):
            if curr > remaining:
                return i

    @staticmethod
    def solution3(chalk: list[int], k: int) -> int:
        summed = list(accumulate(chalk))
        return bisect_right(summed, k % summed[-1])
