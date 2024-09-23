from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [["iiii", 1], ["leetcode", 2], ["zbax", 2], ["dbvmfhnttvr", 5]]

    EXPECTED = [
        36,
        6,
        8,
        5,
    ]

    @staticmethod
    def solution(s: str, k: int) -> int:
        s = "".join(map(lambda x: str(ord(x) - 96), s))
        while k and len(s) > 1:
            s = sum(map(lambda x: int(x), s))
            if k := k - 1:
                s = str(s)
        return int(s)
