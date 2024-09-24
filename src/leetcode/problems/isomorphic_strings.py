from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        ["egg", "add"],
        ["foo", "bar"],
        ["paper", "title"],
    ]

    EXPECTED = [
        True,
        False,
        True,
    ]

    @staticmethod
    def solution(s: str, t: str) -> bool:
        mapping = {}

        for source, target in zip(s, t):
            mapped = mapping.get(source)
            if mapped is not None:
                if mapped != target:
                    return False
                continue
            if target in mapping.values():
                return False
            mapping[source] = target

        return True
