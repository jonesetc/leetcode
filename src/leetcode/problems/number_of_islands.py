from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        ],
        [
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        ],
    ]

    EXPECTED = [
        1,
        3,
    ]

    @staticmethod
    def solution(grid: list[list[str]]) -> int:
        height = len(grid)
        width = len(grid[0])

        count = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == "1":
                    count += 1
                    grid[row][col] = "0"

                    to_visit = [(row, col)]
                    while len(to_visit) > 0:
                        r, c = to_visit.pop()
                        if r - 1 >= 0 and grid[r - 1][c] == "1":
                            grid[r - 1][c] = "0"
                            to_visit.append((r - 1, c))
                        if r + 1 < height and grid[r + 1][c] == "1":
                            grid[r + 1][c] = "0"
                            to_visit.append((r + 1, c))
                        if c - 1 >= 0 and grid[r][c - 1] == "1":
                            grid[r][c - 1] = "0"
                            to_visit.append((r, c - 1))
                        if c + 1 < width and grid[r][c + 1] == "1":
                            grid[r][c + 1] = "0"
                            to_visit.append((r, c + 1))

        return count
