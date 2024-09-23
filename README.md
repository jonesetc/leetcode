# leetcode

Trying to get a job, or maybe I have one now and I'm just messing around.

## Getting started

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- List problems with `uv run leetcode list`
- Run problem with `uv run leetcode run <problem-name>`
  - Run any subset of test cases by adding the indexes at the end of the command (just space separated, no ranges)
- Open problem in browser with `uv run leetcode open <problem-name>`

## Adding new problems

- Copy [template.py](./src/leetcode/problems/template.py) into the same directory with `slug_name_in_snake_case.py`
- Replace `TEST_CASES`, `EXPECTED`, and `solution` with real values for solution
- If a custom judge is required, override the default `judge` implementation
