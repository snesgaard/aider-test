test:
	uv run pytest --cov=src/ --cov-fail-under=100 --cov-report=term-missing  --no-cov-on-fail test/

lint:
	uv run ruff check src/ test/

ci: lint test

sync:
	uv sync

aider:
	OLLAMA_API_BASE=http://127.0.0.1:11434 aider


.PHONY: sync lint test