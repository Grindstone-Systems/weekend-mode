PYTHON ?= python3

.PHONY: all certify generate test verify touch-grass

all: verify

generate:
	$(PYTHON) scripts/weekend_mode.py generate

certify:
	$(PYTHON) scripts/weekend_mode.py certify

test:
	./tests/temporal-boundary-evals.sh
	./tests/friday-soak-evals.sh
	./tests/governance-integrity.sh
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py' -v

verify:
	./tests/generated-artifact-integrity.sh
	$(MAKE) test

touch-grass:
	@$(PYTHON) scripts/weekend_mode.py touch-grass
