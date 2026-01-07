---
name: review-code
description: Review Go code for best practices and Clean Architecture
args:
  - name: path
    description: Path to file or directory to review
    default: .
---

# Review Code

Trigger the `go-reviewer` agent to analyze specific files or directories.

## Trigger
`/review-code [path]`

## Agent
Use the **go-reviewer** agent to perform the code review.

## Workflow

1. Invoke the `go-reviewer` agent with the Task tool.
2. Perform analysis using `golangci-lint` if available.
3. Manual analysis for:
   - Clean Architecture layer violations.
   - Uber Go Style Guide compliance.
   - Proper error handling and wrapping.
   - Concurrency safety.
   - Security vulnerabilities.
4. Output a structured checklist with Pass/Fail/Improvement results.

## Prompt
"Use the go-reviewer agent to review the Go code at '{{args.path}}'. Check for Clean Architecture compliance, Uber style guide, and idiomatic Go patterns. Provide a structured checklist with Pass/Fail results."
