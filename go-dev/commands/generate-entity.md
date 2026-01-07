---
name: generate-entity
description: Generate complete CRUD for a new entity
args:
  - name: name
    description: Entity name (e.g., User, Product)
    required: true
  - name: type
    description: Type of entity (crud, business)
    default: crud
---

# Generate Entity

Generate domain model, usecase, repository, handler, routes, tests, and migration for a specific entity.

## Trigger
`/generate-entity <name> [type]`

## Agent
Use the **go-api** agent to implement all entity layers.

## Workflow

1. Invoke the `go-api` agent with the Task tool.
2. Analyze existing project structure and `main.go`.
3. Generate entity files in appropriate layers following Clean Architecture:
   - `internal/domain/{{name}}.go`
   - `internal/usecase/{{name}}_usecase.go`
   - `internal/adapter/repository/{{name}}_repository.go`
   - `internal/adapter/handler/{{name}}_handler.go`
4. Generate unit tests for each layer.
5. Generate new SQL migration files (up/down) in `migrations/` using `golang-migrate` naming convention (timestamp-based).
6. Auto-register the new routes in `main.go` or the router configuration.
7. Ensure all code follows the Uber Go Style Guide.

## Prompt
"Use the go-api agent to generate a {{args.type}} entity for '{{args.name}}' following Clean Architecture and Uber Go Style Guide. Include domain model, usecase, repository, handler, routes, tests, and database migration. Automatically register the routes in the project."
