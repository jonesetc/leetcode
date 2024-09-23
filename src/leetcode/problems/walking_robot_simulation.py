from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[4, -1, 3], []],
        [[4, -1, 4, -2, 4], [[2, 4]]],
        [[6, -1, -1, 6], []],
    ]

    EXPECTED = [
        25,
        65,
        36,
    ]

    @staticmethod
    def solution(commands: list[int], obstacles: list[list[int]]) -> int:
        obs = set(map(tuple, obstacles))

        curr_dir = (0, 1)
        curr_pos = (0, 0)
        max_dist = 0

        for command in commands:
            if command == -1:
                curr_dir = (curr_dir[1], -curr_dir[0])
            elif command == -2:
                curr_dir = (-curr_dir[1], curr_dir[0])
            else:
                for _ in range(command):
                    new_pos = (
                        curr_pos[0] + curr_dir[0],
                        curr_pos[1] + curr_dir[1],
                    )

                    if new_pos not in obs:
                        curr_pos = new_pos
                    else:
                        break

                max_dist = max(max_dist, curr_pos[0] ** 2 + curr_pos[1] ** 2)

        return max_dist
