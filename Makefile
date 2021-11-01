install:
	python -m pip install --upgrade pip
	pip install -r requeiress.txt

lint:
	pylint -d W0122 *.py

test:
	python -m doctest assault/stats.py

invoke:
	assault http://www.google.com -r 100 -c 10

invoke-to-json:
	assault http://www.google.com -r 100 -c 10 -j assault.json