.PHONY: up
up:
	@docker-compose -f docker-compose.yml up --build -d

.PHONY: uninstall
uninstall:
	@docker-compose -f docker-compose.yml down --remove-orphans --volumes
