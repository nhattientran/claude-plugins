---
name: add-middleware
description: Add middleware to the Go service
---

# Add Middleware

Interactive menu to add common middleware like JWT, CORS, Logger, RateLimiter, and Recovery.

## Trigger
`/add-middleware`

## Agent
Use the **go-api** agent to implement the middleware.

## Workflow

1. Invoke the `go-api` agent with the Task tool.
2. Present an interactive menu with the following options:
   - JWT Authentication
   - CORS (Cross-Origin Resource Sharing)
   - Request/Response Logger
   - Rate Limiter
   - Panic Recovery
3. Collect necessary configuration for the selected middleware (e.g., JWT secret, allowed origins).
4. Implement the middleware in `internal/adapter/middleware/`.
5. Auto-register the middleware in `main.go` or the global router setup.
6. Provide documentation on how to use/configure the middleware.

## Prompt
"Use the go-api agent to add middleware to my Go service. Provide an interactive menu for JWT, CORS, Logger, RateLimiter, and Recovery. Guide me through the implementation and auto-register it in my main.go file."
