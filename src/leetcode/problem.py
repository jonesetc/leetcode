from abc import ABC, ABCMeta, abstractmethod
from typing import Callable, Tuple
from pathlib import PurePath

import click

from .judge import json_judge


class AbstractProblem[T: list, E, S](ABC):
    TEST_CASES: list[T] = NotImplemented
    EXPECTED: list[E] = NotImplemented

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.TEST_CASES is NotImplemented:
            raise ValueError("Must define test cases.")
        if cls.EXPECTED is NotImplemented:
            raise ValueError("Must define expected.")
        if len(cls.TEST_CASES) != len(cls.EXPECTED):
            raise ValueError("There must be an expected for every test case.")

    @staticmethod
    @abstractmethod
    def solution(*args: T) -> S: ...

    @staticmethod
    def judge(test_case_after_solution: T, solution: S, expected: E) -> Tuple[E, bool]:
        return solution, json_judge(solution, expected)

    @staticmethod
    def run_test_case(
        known_test_cases: list[T],
        expected_solutions: list[E],
        solution_func: Callable[..., S],
        judge_func: Callable[[T, S, E], Tuple[E, bool]],
        test_case: int,
    ):
        case = known_test_cases[test_case]
        solution = solution_func(*case)
        expected = expected_solutions[test_case]

        actual, correct = judge_func(case, solution, expected)

        print(f"{case=} {correct=} {expected=} {actual=}")

    @staticmethod
    def run_test_cases(
        run_test_case_func: Callable[[int], None],
        test_cases: list[int],
    ):
        for i in test_cases:
            run_test_case_func(i)


class ProblemCommand(ABCMeta):
    def __new__(cls, name, bases, attrs, *, filename: str):
        if AbstractProblem not in bases:
            raise ValueError("ProblemCommand must implement AbstractProblem.")

        slug = PurePath(filename).stem.replace("_", "-")
        known_test_cases = attrs["TEST_CASES"]
        expected_solutions = attrs["EXPECTED"]
        num_test_cases = len(known_test_cases)

        solution_func = attrs["solution"]
        judge_func = attrs["judge"] if "judge" in attrs else AbstractProblem.judge

        run_test_case_func = lambda test_case: AbstractProblem.run_test_case(
            known_test_cases,
            expected_solutions,
            solution_func,
            judge_func,
            test_case,
        )

        attrs["run_test_cases"] = click.argument(
            "test-cases", nargs=-1, type=click.IntRange(0, num_test_cases - 1)
        )(
            click.command(slug)(
                lambda test_cases: AbstractProblem.run_test_cases(
                    run_test_case_func, test_cases
                )
                if len(test_cases) > 0
                else AbstractProblem.run_test_cases(
                    run_test_case_func, [i for i in range(num_test_cases)]
                )
            )
        )

        return super().__new__(cls, name, bases, attrs)
