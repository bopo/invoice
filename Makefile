# Makefile six

PIP=$(VIRTUAL_ENV)/bin/pip 
PY=$(VIRTUAL_ENV)/bin/python

.PHONY: clean-pyc clean-build docs pack clean clean-others req pep8 req.base req.all server

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-others - remove Thumbs.db, etc file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "pep8 - check style with pycodestyle"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "req - install project requirements"
	@echo "req.update - update project requirements"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"


clean: clean-build clean-others clean-test clean-pyc clean-runtime
distclean: clean-build clean-others clean-pyc clean-test clean-runtime clean-database

clean-database:
	rm -fr database/backups/*
	rm -fr database/fixtrues/*

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -rf '*.tgz'
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.log' -exec rm -f {} +
	find . -name '*.sql' -exec rm -f {} +

clean-others:
	find . -name 'Thumbs.db' -exec rm -f {} +
	find . -name '*.tgz' -exec rm -f {} +
	find . -name 'dump.rdb' -exec rm -f {} +
	find . -name 'celery*.db' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -rf nosetests.html
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf reports/
	rm -rf .tox/
	

clean-runtime:
	rm -fr runtime/**/**

lint:
	# flake8 --ignore=E501,F403,E122 .
	pycodestyle --ignore=E501,F403,E122 **/*.py
	# autopep8 --in-place --aggressive --aggressive --ignore=E501,F403,E122 **/*.py

pack:
	tar zcfv ./pack.tgz .

test:
	DJANGO_SETTINGS_MODULE=config.settings.test $(PY) manage.py test --traceback -v2

test-all:
	tox

coverage:
	coverage run --source vin-delphos manage.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/vin-delphos.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ vin-delphos
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

pip:
	@$(PIP) install -r requirements/base.txt

pip.dev:
	@$(PIP) install -r requirements/dev.txt

pip.pre:
	@$(PIP) install -r requirements/pre.txt

pip.test:
	@$(PIP) install -r tests/requirements.txt

pep8:
	# @pep8 --filename="*.py" --ignore=W --first --show-source --statistics --count
	@pycodestyle .


release: clean req.prod
	@$(PY) manage.py test

serve:
	@$(PY) manage.py runserver

start: clean migrate serve

startup: clean req.prod
	@$(PY) manage.py test

dist: clean
	@$(PY) setup.py sdist
	@$(PY) setup.py bdist_wheel

shell:
	@$(PY) manage.py shell_plus

migrate:
	@$(PY) manage.py migrate

setup: clean req migrate
	@$(PY) manage.py createsuperuser

# DO NOT DELETE
