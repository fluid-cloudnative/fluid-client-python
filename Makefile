.PHONY: setup_build clean release

setup_build:
	python -m pip install --upgrade build
	python -m pip install --upgrade twine

clean:
	rm -rf dist/*

dist: setup_build
	python -m build

release_test: dist
	twine upload --repository testpypi dist/*
