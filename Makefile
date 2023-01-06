PROJECT = $(shell basename $(CURDIR))
DC = docker compose
DCR = ${DC} run --rm --no-deps ${PROJECT}
workdir = euler/$(shell printf '%02d' $(PROB))

.PHONY: init
init: destroy build shell ## Setup project with python resources

.PHONY: destroy
destroy: ## Delete the previous setup
	${DC} down --remove-orphans --rmi local

.PHONY: build
build: ## Build the project
	${DC} build ${PROJECT}

.PHONY: up
up: ## Start the service
	${DC} up -d

.PHONY: shell
shell: ##- Run a bash shell
	${DCR} bash

.PHONY: run
run: ## Run the project
	${DCR} python ${workdir}/code.py

.PHONY: prob
prob: ## Create a new problem
	mkdir -p ${workdir}
	cp -n template/* ${workdir}/
	git add ${workdir}

.PHONY: what
what: ## What prob is it?
	@echo ${workdir}
