.PHONY: test check

test:
	python -m unittest discover -s tests -v

check:
	python -m py_compile asimov_meter.py tests/test_asimov_meter.py
	python -m unittest discover -s tests -v
