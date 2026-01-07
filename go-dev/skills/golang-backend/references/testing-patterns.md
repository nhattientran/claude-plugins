# Testing Patterns

## Table-Driven Tests
The idiomatic Go way (Uber Style Guide).

```go
func TestCalculate(t *testing.T) {
    tests := []struct {
        name     string
        input    int
        expected int
        wantErr  bool
    }{
        {"success", 1, 2, false},
        {"invalid", -1, 0, true},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := Calculate(tt.input)
            if (err != nil) != tt.wantErr {
                t.Errorf("Calculate() error = %v, wantErr %v", err, tt.wantErr)
                return
            }
            if got != tt.expected {
                t.Errorf("Calculate() got = %v, want %v", got, tt.expected)
            }
        })
    }
}
```

## Mocking with Testify
Use `testify/mock` for interface mocking.

```go
type MockRepo struct {
    mock.Mock
}

func (m *MockRepo) Get(id string) (*User, error) {
    args := m.Called(id)
    return args.Get(0).(*User), args.Error(1)
}
```

## Integration Tests
Use Docker (testcontainers-go) or a test database.
Separate with build tags: `// +build integration`

```go
func TestUserRepository_Save(t *testing.T) {
    if testing.Short() {
        t.Skip("skipping integration test")
    }
    // ... setup DB and test
}
```
