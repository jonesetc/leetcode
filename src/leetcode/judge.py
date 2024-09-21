from json import dumps


def simple_judge[T](actual: T, expected: T):
    return actual == expected


def json_judge[T](actual: T, expected: T):
    return dumps(expected) == dumps(actual)


def list_judge[T](actual: list[T], expected: list[T], *, ordered: bool = True):
    return len(actual) == len(expected) and all(
        a == e
        for a, e in zip(
            actual if ordered else sorted(actual),
            expected if ordered else sorted(expected),
        )
    )


def beginning_list_judge[T](
    actual: list[T], expected: list[T], n, *, ordered: bool = True
):
    return (
        len(expected) == n
        and len(actual) >= n
        and list_judge(actual[:n], expected, ordered=ordered)
    )
