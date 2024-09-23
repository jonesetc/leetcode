from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
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

    @staticmethod
    def solution(s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        return all(c == r for c, r in zip(cleaned, reversed(cleaned)))

    @staticmethod
    def solution2(s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        length = len(cleaned)

        for i in range(0, length // 2):
            if cleaned[i] != cleaned[length - i - 1]:
                return False

        return True

    @staticmethod
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
