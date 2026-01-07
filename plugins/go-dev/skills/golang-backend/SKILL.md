---
name: golang-backend
description: Build production-ready Go backend services with Clean Architecture, REST APIs, gRPC, microservices, and database integration. Use when building a Go backend, setting up Clean Architecture, creating REST APIs with Gin/Echo/Fiber, implementing GORM or sqlx, adding authentication middleware, or writing Go tests.
---

# Golang Backend Development

Develop scalable Go backends following Clean Architecture and Uber Go Style Guide.

## Core Capabilities

1. **Build a Go backend** - Initialize project with Clean Architecture.
2. **Setup Clean Architecture** - Organize code into Domain, Usecase, Adapter, and Infrastructure layers.
3. **Create REST API with Gin** - Implement high-performance HTTP endpoints.
4. **Implement GORM** - Integrate ORM for database operations and migrations.
5. **Develop gRPC services** - Define and implement protobuf-based services.
6. **Apply Uber Go Style Guide** - Ensure idiomatic and consistent Go code.
7. **Configure middleware** - Implement JWT auth, CORS, and logging.
8. **Write Go tests** - Create table-driven unit and integration tests.

## Agents

- **go-architect**: Designs project architecture, file trees, and implementation plans.
- **go-api**: Implements REST API endpoints with validation, error handling, and documentation.
- **go-reviewer**: Performs comprehensive code reviews for Clean Architecture and Uber style compliance.

## Commands

- `/scaffold-project [name]` - Bootstrap a new Go project with Clean Architecture.
- `/generate-entity <name> [type]` - Generate CRUD or business entity layers.
- `/add-middleware` - Interactive menu to add common Go middleware.
- `/add-endpoint <entity> <method> [path]` - Add new endpoint to an existing entity.
- `/review-code [path]` - Trigger code review for specific path.

## References

- [clean-architecture.md](references/clean-architecture.md) - Layer rules and dependency flow.
- [rest-api-patterns.md](references/rest-api-patterns.md) - Gin/Echo/Fiber usage and validation.
- [grpc-patterns.md](references/grpc-patterns.md) - Service definitions and implementation.
- [database-patterns.md](references/database-patterns.md) - GORM/sqlx and repository pattern.
- [middleware-patterns.md](references/middleware-patterns.md) - Auth, logging, and recovery.
- [config-patterns.md](references/config-patterns.md) - Configuration with viper and godotenv.
- [testing-patterns.md](references/testing-patterns.md) - Mocking and test strategies.

## Automation

- `python scripts/generate_handler.py <entity>` - Generate CRUD handler boilerplate.

## Architecture

```
Infrastructure (DB, Config) -> Adapter (Handlers, Repos) -> Usecase (Logic) -> Domain (Entities)
```

- **Domain**: No external dependencies.
- **Usecase**: Business rules, defines interfaces.
- **Adapter**: Implements interfaces (HTTP, DB).
- **Infrastructure**: Third-party tools and frameworks.
