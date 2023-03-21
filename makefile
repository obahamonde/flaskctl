
install:
	sudo apt install curl
	sudo apt install python3-pip
	sudo apt install python3-venv
	sudo apt install python-is-python3

dev:
	source venv/bin/activate
	gunicorn app:app --reload --bind 0.0.0.0:8080

test:
	source venv/bin/activate
	pip install --upgrade pytest
	pytest