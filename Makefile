dev:
	docker compose -f infrastructure/docker-compose.yml up --build

index:
	python scripts/index_repo.py ./repo