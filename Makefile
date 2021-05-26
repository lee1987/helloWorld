
PYTHON := python
DOCKER := docker
DOCKER_COMPOSE := docker-compose


GIT_COMMIT := $(shell git rev-parse --short HEAD 2> /dev/null || echo "no-revision")
GIT_COMMIT_MESSAGE := $(shell git show -s --format='%s' 2> /dev/null | tr ' ' _ | tr -d "'")
GIT_TAG := $(shell git describe --tags 2> /dev/null || echo "no-tag")
GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD 2> /dev/null || echo "no-branch")
BUILD_TIME := $(shell date +%FT%T%z)

help:                        ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

unittest:                    ## Run unit test.
	$(PYTHON) -m pytest tests/unit_tests

behavetest:                  ## Run behave test.
	$(PYTHON) -m behave tests/behave_tests/features

prune:                       ## Removes all stopped containers.
	$(DOCKER) container prune -f

build-image:                 ## Build the docker image.
	$(DOCKER_COMPOSE) build --no-cache app

run-containers: build-image  ## Build the image then run the system.
	$(DOCKER_COMPOSE) up -d
