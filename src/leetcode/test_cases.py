def filter_and_zip[T, E](
    test_cases: list[T], expected_answers: list[E], indices: list[int] | None
) -> iter(tuple[T, E]):
    if indices is None or len(indices) == 0:
        return zip(test_cases, expected_answers, strict=True)
    else:
        return zip(
            [test_cases[i] for i in indices],
            [expected_answers[i] for i in indices],
            strict=True,
        )
