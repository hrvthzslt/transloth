DC_EXITS := $(shell docker compose > /dev/null 2>&1 ; echo $$?)

ifeq ($(DC_EXITS),0)
	DOCKER_COMPOSE = docker compose
else
	DOCKER_COMPOSE = docker-compose
endif

help:
	@grep -h -E '^[a-zA-Z0-9_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

start: # Start the environment
	$(DOCKER_COMPOSE) up -d;

stop: # Stop the environment
	$(DOCKER_COMPOSE) down;

build: # Build the stack
	$(DOCKER_COMPOSE) build;

shell-ollama: # Open interactive shell
	$(DOCKER_COMPOSE) exec ollama bash;

logs-ollama: # Show ollama logs
	$(DOCKER_COMPOSE) logs ollama -f;

shell-web: # Open interactive shell
	$(DOCKER_COMPOSE) exec web sh;

logs-web: # Show ollama logs
	$(DOCKER_COMPOSE) logs web -f;

test-request: # Run a test request
	curl -X POST "http://localhost:8000/translate" -H "Content-Type: application/json" -d '{"text": "The quick brown fox jumps over the lazy dog", "source": "english", "target": "italian"}'
	@echo \-
	curl -X POST "http://localhost:8000/translate" -H "Content-Type: application/json" -d '{"text": "La veloce volpe marrone salta sopra il cane pigro", "source": "italian", "target": "english"}'

lint: # Run linter
	$(DOCKER_COMPOSE) exec web ruff check;
	$(DOCKER_COMPOSE) exec web ruff format --check;

fix: # Fix linting problems
	$(DOCKER_COMPOSE) exec web ruff check --fix;
	$(DOCKER_COMPOSE) exec web ruff format;
