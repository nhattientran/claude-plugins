# Clean Architecture Patterns

## Layer Responsibilities

### 1. Domain Layer (`internal/domain`)
- **Entities**: Business objects (structs).
- **Errors**: Domain-specific error constants.
- **Rules**: NO external dependencies. No frameworks.

### 2. Usecase Layer (`internal/usecase`)
- **Logic**: Application-specific business rules.
- **Interfaces**: Defines what the layer needs (e.g., `UserRepository` interface).
- **DTOs**: Data Transfer Objects for input/output.

### 3. Adapter Layer (`internal/adapter`)
- **Handlers**: HTTP/gRPC controllers. Convert transport data to DTOs.
- **Repositories**: Database implementations of Usecase interfaces.
- **Presenters**: Format output for the client.

### 4. Infrastructure Layer (`internal/infrastructure`)
- **DB**: Database connection setup.
- **Config**: Environment variable parsing and configuration loading. This is where `viper` and `godotenv` logic resides.
- **Logger**: Logging implementation.

## Configuration Flow

1. **Initialization**: Configuration is loaded in `main.go` using the infrastructure's config package.
2. **Injection**: The configuration (or relevant parts of it) is injected into other infrastructure components (like DB or Logger) and adapters (like HTTP handlers).
3. **Application**: Business logic in Usecases remains agnostic of where configuration comes from, receiving only necessary values via their constructors.

```go
// main.go
func main() {
    cfg, err := config.NewConfig()
    if err != nil {
        log.Fatalf("failed to load config: %v", err)
    }

    db, err := infrastructure.NewDatabase(cfg.Database)
    // ...
}
```

## Dependency Rule
Dependencies must point **inward** only:
`Infrastructure -> Adapter -> Usecase -> Domain`

## Dependency Injection
Always use Constructor Injection (Uber Style Guide):

```go
func NewUserUsecase(repo domain.UserRepository) *UserUsecase {
    return &UserUsecase{repo: repo}
}
```
