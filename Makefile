.PHONY: venv clean test lint

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate

clean:
	rm -rf venv
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

lint: venv
	. venv/bin/activate; \
	pylint src/

test: venv
	. venv/bin/activate; \
	pytest

build-lambda: venv
	. venv/bin/activate; \
	sam build -m requirements.txt

run-lambda: venv
	. venv/bin/activate; \
	sam local invoke -e events/event.json LambdaFunction --docker-network host
