POETRY=poetry
PYTEST=$(POETRY) run pytest
MYPY=$(POETRY) run mypy
BLACK=$(POETRY) run black
ISORT=$(POETRY) run isort
PYLINT=$(POETRY) run pylint
UVICORN=$(POETRY) run uvicorn
PACKAGE=app

install:
	$(POETRY) install
	$(POETRY_EXPORT)

update:
	$(POETRY) update
	$(POETRY_EXPORT)

test: install
	$(MYPY) ./${PACKAGE}/
	$(PYTEST) -vv

fmt:
	$(ISORT) ./${PACKAGE} ./tests
	$(BLACK) ./${PACKAGE} ./tests

lint:
	$(PYLINT) ./${PACKAGE} ./tests

dev:
	${UVICORN} main:app --reload