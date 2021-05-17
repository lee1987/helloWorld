
PYTHON := python
DOCKER := docker
DOCKER_COMPOSE := docker-compose


GIT_COMMIT := $(shell git rev-parse --short HEAD 2> /dev/null || echo "no-revision")
GIT_COMMIT_MESSAGE := $(shell git show -s --format='%s' 2> /dev/null | tr ' ' _ | tr -d "'")
GIT_TAG := $(shell git describe --tags 2> /dev/null || echo "no-tag")
GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD 2> /dev/null || echo "no-branch")
BUILD_TIME := $(shell date +%FT%T%z)


unittest:
	$(PYTHON) -m pytest tests/unit_tests

behavetest:
	$(PYTHON) -m behave tests/behave_tests/features

prune:
	$(DOCKER) container prune -f

build-image:
	$(DOCKER_COMPOSE) build --no-cache app

run-containers: build-image
	$(DOCKER_COMPOSE) up -d
