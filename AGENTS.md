# AGENTS.md

## Commands
- Install: `make sync`
- Test : `make test`
- Lint: `make lint`
Run test and lint after every change. Both must pass before you report done.

## Layout
- `src/aider_test` -- Library souce code goes here.
- `test/` -- Test code goes here.

## Conventions
- All functions must be type annotated.
- All functions must have a docstring.
- Use pytest for testing.
- All functions must have a unit test.

## Never
- Never modify tests to make them pass. Fix the code.
- Never add a dependency without asking.
- Never touch `.venv` or Makefile.
- Never modify code that is unrelated to the current task.