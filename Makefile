test:
	uv run pytest test/

lint:
	uv run ruff check src/ test/

ci: lint test

sync:
	uv sync

.PHONY: sync lint test