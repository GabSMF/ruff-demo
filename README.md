# Ruff Demo With `uv`

This is a very small project to demonstrate Ruff working with:

- `pyproject.toml` for configuration
- `uv` for environment management and running commands

The file [src/ruff_demo/student.py](/home/gabriel/Documents/Projects/ruff-demo/src/ruff_demo/student.py) is intentionally messy so you can show Ruff finding problems, fixing lint issues, and formatting the code.

## Setup

```bash
uv sync
```

## Show Ruff finding issues

```bash
uv run ruff check .
```

## Auto-fix lint problems

```bash
uv run ruff check . --fix
```

## Format the code

```bash
uv run ruff format .
```

## Confirm everything is clean

```bash
uv run ruff check .
uv run ruff format . --check
```

## Optional: run the example

```bash
uv run python -c "from ruff_demo import Student; print(Student('Ana', [8, 9, 10]).summary())"
```
