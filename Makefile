##@ General

help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Run

build: ## Build
	@docker compose -f docker-compose-py.yaml build flink-master flink-task-manager

up: build ## Up
	@docker compose -f docker-compose-py.yaml up --build

shell:
	@docker compose -f docker-compose-shell.yaml build flink-shell
	@docker compose -f docker-compose-shell.yaml run flink-shell