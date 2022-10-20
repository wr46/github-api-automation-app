OPTION?=--help

init:
	@[ ! -f '.env' ] && cp .env.example .env && echo 'You can now setup .env file' || true

install: init
	pipenv --python $(shell which python)
	pipenv install -e .

run:
	pipenv run python github_automation/main.py ${OPTION}

uninstall:
	pipenv --rm