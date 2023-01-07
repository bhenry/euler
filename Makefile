PROJECT = $(shell basename $(CURDIR))
DC = docker compose
DCR = ${DC} run --rm --no-deps ${PROJECT}
workfile = euler/$(shell printf '%03d' $(PROB)).py

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
	${DCR} python ${workfile}

.PHONY: prob
prob: ## Create a new problem
	touch ${workfile}
	git add ${workfile}

.PHONY: what
what: ## What prob is it?
	@echo ${workfile}
