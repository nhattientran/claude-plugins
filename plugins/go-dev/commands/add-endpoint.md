---
name: add-endpoint
description: Add a new API endpoint to an existing entity
args:
  - name: entity
    description: Target entity name
    required: true
  - name: method
    description: HTTP method (GET, POST, PUT, DELETE)
    required: true
  - name: path
    description: API path (optional)
---

# Add Endpoint

Generate handler method, request/response structs with validation, and register the route for a new endpoint.

## Trigger
`/add-endpoint <entity> <method> [path]`

## Agent
Use the **go-api** agent to implement the endpoint.

## Workflow

1. Invoke the `go-api` agent with the Task tool.
2. Verify the existence of the target entity and its handler.
3. Generate request and response structs with appropriate tags (json, validate).
4. Implement the handler method in `internal/adapter/handler/{{entity}}_handler.go`.
5. Implement the usecase method and domain interface if needed.
6. Register the new route in the entity's router configuration.
7. Follow Uber Go Style Guide for error handling and naming.

## Prompt
"Use the go-api agent to add a {{args.method}} endpoint for the '{{args.entity}}' entity at path '{{args.path}}'. Generate the handler method, request/response structs with validation, and register the route."
