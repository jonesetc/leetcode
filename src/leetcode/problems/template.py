from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [1],
        [2],
        [3],
    ]

    EXPECTED = [
        1,
        2,
        3,
    ]

    @staticmethod
    def solution(expected: int) -> int:
        return expected
