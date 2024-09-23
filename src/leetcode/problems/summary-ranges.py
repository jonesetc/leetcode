from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[0, 1, 2, 4, 5, 7]],
        [[0, 2, 3, 4, 6, 8, 9]],
    ]

    EXPECTED = [
        ["0->2", "4->5", "7"],
        ["0", "2->4", "6", "8->9"],
    ]

    @staticmethod
    def solution(nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        runs = []
        run = nums[0]
        run_diff = nums[0]

        for i, element in enumerate(nums):
            current_diff = element - i

            if run_diff != current_diff:
                run_length = i - (run - run_diff)
                if run_length > 1:
                    runs.append(f"{run}->{run + run_length - 1}")
                else:
                    runs.append(str(run))

                run = element
                run_diff = current_diff
        else:
            run_length = len(nums) - (run - run_diff)
            if run_length > 1:
                runs.append(f"{run}->{run + run_length - 1}")
            else:
                runs.append(str(run))

        return runs
