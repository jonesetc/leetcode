from collections import defaultdict

from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]],
        [[2, 3, 4], [3, 4, 3]],
    ]

    EXPECTED = [
        3,
        -1,
    ]

    @staticmethod
    def solution(gas: list[int], cost: list[int]) -> int:
        segments = {}
        segment_start = 0
        segment_required = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            if segment_required < 0:
                segments[segment_start] = segment_required
                segment_start = i
                segment_required = 0

            segment_required += g - c
        else:
            segments[segment_start] = segment_required

        if sum(segments.values()) < 0:
            return -1

        return sorted(segments, key=segments.get, reverse=True)[0]

    @staticmethod
    def solution2(gas: list[int], cost: list[int]) -> int:
        segments = defaultdict(int)
        segment_start = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            if segments[segment_start] < 0:
                segment_start = i
            segments[segment_start] += g - c

        if sum(segments.values()) < 0:
            return -1

        return sorted(segments, key=segments.get, reverse=True)[0]
