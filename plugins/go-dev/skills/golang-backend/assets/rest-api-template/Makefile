.PHONY: run migrate-create migrate-up migrate-down

run:
	go run cmd/api/main.go

migrate-create:
	migrate create -ext sql -dir migrations -seq $(name)

migrate-up:
	migrate -path migrations -database "$(DB_DSN)" -verbose up

migrate-down:
	migrate -path migrations -database "$(DB_DSN)" -verbose down
