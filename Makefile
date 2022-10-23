OPTION?=--help
IMAGE=github-automation-app:local

init:
	@[ ! -f '.env' ] && cp .env.example .env && echo 'You can now setup .env file' || true

install:
	@pipenv --python $(shell which python)
	@pipenv install -e .

run: init
	@pipenv run python github_automation/main.py ${OPTION}

uninstall:
	@pipenv --rm

docker-build:
	@docker build -t ${IMAGE} .

docker-run: init
	@docker run --rm --env-file .env ${IMAGE} ${OPTION}

docker-remove:
	@docker rmi ${IMAGE}

docker-remove-dangling:
	@docker rmi $$(docker images --filter "dangling=true" -q --no-trunc)
