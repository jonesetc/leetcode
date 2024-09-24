from collections import Counter

from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        ["a", "b"],
        ["aa", "ab"],
        ["aa", "aab"],
    ]

    EXPECTED = [
        False,
        False,
        True,
    ]

    # noinspection PyPep8Naming
    @staticmethod
    def solution(ransomNote: str, magazine: str) -> bool:
        ransom_note_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)

        return all(
            map(
                lambda letter: magazine_counts.get(letter, 0)
                >= ransom_note_counts[letter],
                ransom_note_counts,
            )
        )
