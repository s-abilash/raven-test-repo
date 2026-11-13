# Session design — small test project

## Goal
A tiny, self-contained Python project for testing the repo's tooling and workflow
(Raven hooks, sign-off, commits). Simple math calculator. Standard library only, so no new dependencies
need approval.

## Scope
- app/**
- tests/**
- README.md
- design.md

## Plan
- `app/__init__.py` — package marker
- `app/calculator.py` — add / subtract / multiply / divide (divide raises on zero)
- `app/main.py` — small CLI entry point (`python -m app.main add 2 3`)
- `tests/test_calculator.py` — `unittest` suite
- `README.md` — what it is and how to run it

## Acceptance
- `python -m unittest discover -s tests` passes
- `python -m app.main add 2 3` prints `5.0`
- Functions have type hints and docstrings, and use `logging` (no `print` outside the CLI)
- No third-party imports
