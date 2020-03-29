
setup:
	rm -rf venv
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -e .
	venv/bin/pip install -r requirements-dev.txt

test:
	./scripts/run_tests

.PHONY: build
build:
	python3 setup.py sdist bdist_wheel
