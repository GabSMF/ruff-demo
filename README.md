# Ruff Demo With `uv`

This repository is intentionally messy so you can demonstrate Ruff across more than
one Python module, following the official documentation:

- <https://docs.astral.sh/ruff/>

The project uses:

- `pyproject.toml` for Ruff configuration
- `uv` for environment management and running commands

The demo shows Ruff working as a linter with `ruff check`, as an auto-fixer with
`ruff check --fix`, and as a formatter with `ruff format`.

The files [src/ruff_demo/student.py](/home/gabriel/Documents/Projects/ruff-demo/src/ruff_demo/student.py)
and [src/ruff_demo/classroom.py](/home/gabriel/Documents/Projects/ruff-demo/src/ruff_demo/classroom.py)
contain intentional problems so you can show Ruff working on a whole repository.

## What This Demo Shows

- import sorting and cleanup
- unused import removal
- formatting of badly spaced code
- modernization rules from `pyupgrade`
- formatting of Python code examples inside docstrings

## Setup

```bash
uv sync
```

## Show Ruff finding issues

```bash
uv run ruff check .
```

## Auto-fix lint problems Ruff can handle safely

```bash
uv run ruff check . --fix
```

## Format the repository

```bash
uv run ruff format .
```

## Inspect what changed

```bash
git diff
```

## Confirm everything is clean

```bash
uv run ruff check .
uv run ruff format . --check
```

## Block commits when Ruff fails

This repo includes a Git `pre-commit` hook in `.githooks/pre-commit`.
Enable it for this clone with:

```bash
git config core.hooksPath .githooks
```

After that, every `git commit` will run:

```bash
uv run ruff check .
uv run ruff format . --check
```

If either command fails, Git aborts the commit.

## Examples To Point Out During The Demo

- `student.py` includes unsorted imports, old `typing` syntax, `.format(...)`, and
  inconsistent spacing.
- `classroom.py` gives you a second module so `ruff check .` scans the package, not just
  a single file.
- The docstring in `classroom.py` contains a deliberately ugly Python code block that
  Ruff can format because `docstring-code-format = true`.

## Optional: run the example after fixing and formatting

```bash
uv run python -c "from ruff_demo import Student, build_honor_roll, render_classroom_report; students = [Student('Ana', [10, 9, 8], nickname='Aninha'), Student('Bruno', [7, 8, 7])]; print(build_honor_roll(students)); print(render_classroom_report(students))"
```
