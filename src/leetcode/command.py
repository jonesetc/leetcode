from pathlib import PurePath


def get_problem_name(filename: str) -> str:
    return PurePath(filename).stem.replace("_", "-")
