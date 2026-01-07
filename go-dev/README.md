# Go Dev Plugin

Comprehensive toolkit for building production-ready Go backend services with Clean Architecture patterns, REST APIs, and database integration.

## Features

- **Project Scaffolding**: Bootstrap new Go projects with Clean Architecture structure
- **Code Generation**: Generate entities, endpoints, and middleware with complete layer implementation
- **Architecture Guidance**: Design patterns and best practices for scalable Go backends
- **Code Review**: Automated review for Clean Architecture compliance and Go best practices
- **Framework Support**: Gin (default), Echo, Fiber
- **Config Management**: Viper and GoDotEnv
- **Migrations**: Golang-migrate
- **Database Integration**: GORM (default) and sqlx with PostgreSQL, MySQL, SQLite
- **Style Compliance**: Adheres to Uber Go Style Guide

## Installation

### Local Development
```bash
cc --plugin-dir C:\Users\nhatt\Documents\claude\go-dev
```

### Permanent Installation
Copy the plugin to your Claude plugins directory:
```bash
mkdir -p ~/.claude/plugins/go-dev
cp -r C:\Users\nhatt\Documents\claude\go-dev/* ~/.claude/plugins/go-dev/
```

## Usage

### Skills
- **golang-backend**: Automatically activates when working with Go backend development tasks. Provides knowledge on Clean Architecture, REST/gRPC patterns, and testing.

### Commands
- `/go-dev:scaffold-project [name]` - Create new Go project with Clean Architecture (default name: `my-go-service`)
- `/go-dev:generate-entity <name> [type]` - Generate complete CRUD for new entity (type: `crud` or `business`)
- `/go-dev:add-middleware` - Interactive menu to add middleware (JWT, CORS, Logger, RateLimiter, Recovery)
- `/go-dev:add-endpoint <entity> <method> [path]` - Add new endpoint to an existing entity
- `/go-dev:review-code [path]` - Trigger code review for specific path using `go-reviewer`

### Agents
- **go-architect**: Designs project architecture, file trees, database schemas, and API contracts. Trigger by asking "design a Go service" or "plan a feature".
- **go-api**: Implements REST API endpoints with validation, error handling, and OpenAPI documentation. Trigger by asking "create an API" or "implement endpoint".
- **go-reviewer**: Comprehensive code review for Go best practices, Clean Architecture, and Uber style compliance. Triggers after task completion or via `/review-code`.

## Configuration

Create `.claude/go-dev.local.md` in your project for custom preferences:

```markdown
# Go Dev Settings

## Framework
- Default: Gin
- Options: Gin, Echo, Fiber

## Database
- Default: PostgreSQL
- Options: PostgreSQL, MySQL, SQLite

## ORM
- Default: GORM
- Options: GORM, sqlx

## Code Style
- Guide: Uber Go Style Guide
- Error Handling: Wrapped with context
```

## Project Structure

Generated projects follow Clean Architecture:

```
myapp/
├── cmd/api/main.go           # Entry point, dependency injection
├── internal/
│   ├── domain/               # Business entities (no external deps)
│   ├── usecase/              # Business logic, interfaces
│   ├── adapter/
│   │   ├── handler/          # HTTP handlers
│   │   ├── repository/       # Database implementations
│   │   └── middleware/       # HTTP middleware
│   └── infrastructure/       # Config, DB, logger
├── migrations/               # Database migrations
├── docker-compose.yml
├── Makefile
└── go.mod
```

## License

MIT
