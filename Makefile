# Python linting, formatting.
.PHONY: format_check format

format_check:
	python -m isort django_app --check-only --diff --profile=black
	python -m isort telegram_bot --check-only --diff --profile=black
	python -m black django_app --fast --check
	python -m black telegram_bot --fast --check

format:
	python -m isort django_app --profile=black
	python -m isort telegram_bot --profile=black
	python -m black django_app
	python -m black telegram_bot