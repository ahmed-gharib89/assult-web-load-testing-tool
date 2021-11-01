install:
	python -m pip install --upgrade pip
	pip install -r requeiress.txt

lint:
	pylint -d W0122 *.py

test:
	python -m doctest assault/stats.py -v