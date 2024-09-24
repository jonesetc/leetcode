from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ],
        [
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ],
    ]

    EXPECTED = [
        True,
        False,
    ]

    @staticmethod
    def solution(board: list[list[str]]) -> bool:
        for i in range(9):
            row_seen = set()
            col_seen = set()
            box_seen = set()
            for j in range(9):
                match row_cell := board[i][j]:
                    case ".":
                        pass
                    case _:
                        if row_cell in row_seen:
                            return False
                        row_seen.add(row_cell)

                match col_cell := board[j][i]:
                    case ".":
                        pass
                    case _:
                        if col_cell in col_seen:
                            return False
                        col_seen.add(col_cell)

                match box_cell := board[((i // 3) * 3) + (j // 3)][
                    ((i % 3) * 3) + (j % 3)
                ]:
                    case ".":
                        pass
                    case _:
                        if box_cell in box_seen:
                            return False
                        box_seen.add(box_cell)

        return True
