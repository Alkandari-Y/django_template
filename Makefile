.PHONY: install
install:
	poetry install --no-root

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: migrate
migrate:
	poetry run python -m source.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m source.manage makemigrations

.PHONY: update
update: install migrate migrations install-pre-commit ;

.PHONY: runserver
runserver:
	poetry run python -m source.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m source.manage createsuperuser
