from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[[1, 3], [2, 6], [8, 10], [15, 18]]],
        [[[1, 4], [4, 5]]],
    ]

    EXPECTED = [
        [[1, 6], [8, 10], [15, 18]],
        [[1, 5]],
    ]

    @staticmethod
    def solution(intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])

        merged = []
        current = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= current[1]:
                current[0] = min(current[0], interval[0])
                current[1] = max(current[1], interval[1])
            else:
                merged.append(current)
                current = interval
        else:
            merged.append(current)

        return merged
