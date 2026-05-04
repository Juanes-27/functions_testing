install: 
	pip install --upgrade pip  && pip install -r requirements.txt && python -m textblob.download_corpora

test:
	python -m pytest -vv  --cov=nlplogic test_corenlp.py

lint:
	pylint --disable=R,C nlplogic/*.py

format:
	python -m black *.py nlplogic

all:
	install lint test

