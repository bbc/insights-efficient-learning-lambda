.PHONY: venv clean test lint

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -e .
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate

clean:
	rm -rf venv
	rm -rf .aws-sam
	rm -r .pytest_cache
	rm -r .coverage
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

lint: venv
	. venv/bin/activate; \
	pylint src/

test: venv
	. venv/bin/activate; \
	pytest -s --cov=src/ test/ --cov-report term-missing -v

docstring_test: venv
	. venv/bin/activate; \
	pytest -s test/test_docstrings.py -v -m docstring_test

validation_test: venv
	. venv/bin/activate; \
	pytest -s test/ -v -m validation_$(feature_name)

feature_test: venv
	. venv/bin/activate; \
	pytest -s test/ -v -m feature_$(feature_name)

fint_test: venv
	. venv/bin/activate; \
	pytest -s test/ -v -m fint_$(feature_name)

bint_test: venv
	. venv/bin/activate; \
	pytest -s test/ -v -m bint_$(feature_name)

functionality_test: venv
	. venv/bin/activate; \
	pytest -s test/ -v -m functionality_$(feature_name)

load-test: 
	npm i artillery
	artillery run -e test test/loadtest/quizzes.yaml

build-lambda: venv
	. venv/bin/activate; \
	sam build -m requirements.txt --use-container

run-lambda: venv
	. venv/bin/activate; \
	sam local invoke -e events/event.json --docker-network host EfficientLearningFunction

build-infra:
	make -C infrastructure all