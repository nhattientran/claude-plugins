---
name: scaffold-project
description: Bootstrap a new Go project with Clean Architecture
args:
  - name: name
    description: Project name
    default: my-go-service
---

# Scaffold Go Project

Initialize a new Go project with Clean Architecture, Gin, GORM (PostgreSQL), Docker Compose, and Makefile. Module path will be `github.com/nhattientran/{{args.name}}`.

## Trigger
`/scaffold-project [name]`

## Agent
Use the **go-architect** agent to design and scaffold the project structure.

## Workflow

1. Invoke the `go-architect` agent with the Task tool.
2. Ask for preferred framework (Gin, Echo, Fiber) and ORM (GORM, sqlx).
3. Design the project architecture following Clean Architecture.
4. Copy base templates from `skills/golang-backend/assets/rest-api-template/`.
5. Initialize `go mod init github.com/nhattientran/{{args.name}}`.
6. Generate `docker-compose.yml` for PostgreSQL and Redis.
7. Create a `Makefile` with common tasks (build, run, test, migrate) using `golang-migrate`.
8. Set up the configuration management using `viper` and `godotenv` in `internal/infrastructure/config/`.
9. Set up the directory structure:
   - `cmd/api/main.go`
   - `internal/domain/`
   - `internal/usecase/`
   - `internal/adapter/handler/`
   - `internal/adapter/repository/`
   - `internal/infrastructure/config/`
   - `migrations/`

## Prompt
"Use the go-architect agent to scaffold a new Go backend project named {{args.name}} with module path github.com/nhattientran/{{args.name}}. Use Clean Architecture and the following tech stack: Gin for the web framework, GORM for the ORM with PostgreSQL. Use viper and godotenv for configuration. Use golang-migrate for database migrations. Include a Docker Compose file and a Makefile."
