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