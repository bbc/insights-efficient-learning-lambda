SOURCES := $(shell echo src/*.py)
TARGETS := $(patsubst src/%.py,templates/%.json,$(SOURCES))

all: $(TARGETS)

clean:
	rm -f $(TARGETS)

templates/%.json: src/%.py venv
	./venv/bin/python $< > $@

venv:
	test -d venv || virtualenv venv
	. venv/bin/activate && \
		pip install awacs troposphere