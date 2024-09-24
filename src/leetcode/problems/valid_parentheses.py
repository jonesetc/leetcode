from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        ["()"],
        ["()[]{}"],
        ["(]"],
        ["([])"],
    ]

    EXPECTED = [
        True,
        True,
        False,
        True,
    ]

    @staticmethod
    def solution(s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case "(" | "[" | "{":
                    stack.append(c)
                case _:
                    if len(stack) == 0:
                        return False
                    match (stack.pop(), c):
                        case ("(", ")") | ("[", "]") | ("{", "}"):
                            continue
                        case _:
                            return False

        return len(stack) == 0
