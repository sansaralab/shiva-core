all:
	@echo "- compose"
	@echo "- compose-stop"

compose:
	docker-compose up -d

compose-stop:
	docker-compose stop
