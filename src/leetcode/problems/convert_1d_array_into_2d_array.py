from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[1, 2, 3, 4], 2, 2],
        [[1, 2, 3], 1, 3],
        [[1, 2], 1, 1],
    ]

    EXPECTED = [
        [[1, 2], [3, 4]],
        [[1, 2, 3]],
        [],
    ]

    @staticmethod
    def solution(original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        else:
            return [original[i : i + n] for i in range(0, len(original), n)]

    @staticmethod
    def solution2(original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        else:
            return list(zip(*([iter(original)] * n)))
