# Database Patterns

## GORM Usage

### Model Definition
Use `gorm` tags and `time.Time` for timestamps.

```go
type User struct {
    ID        string         `gorm:"primaryKey;type:uuid"`
    Email     string         `gorm:"uniqueIndex;not null"`
    CreatedAt time.Time
    UpdatedAt time.Time
    DeletedAt gorm.DeletedAt `gorm:"index"`
}
```

### Repository Pattern

```go
type GormUserRepository struct {
    db *gorm.DB
}

func (r *GormUserRepository) Save(ctx context.Context, user *domain.User) error {
    return r.db.WithContext(ctx).Create(user).Error
}
```

## sqlx Usage
For raw SQL enthusiasts.

```go
func (r *SqlxUserRepository) GetByID(ctx context.Context, id string) (*domain.User, error) {
    var user domain.User
    err := r.db.GetContext(ctx, &user, "SELECT * FROM users WHERE id = $1", id)
    return &user, err
}
```

## Migrations

Use `golang-migrate` for versioned migrations. Store migration files in the `./migrations` folder.

### CLI Usage

Install the CLI:
```bash
go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@latest
```

Create new migrations:
```bash
migrate create -ext sql -dir migrations -seq create_users_table
```

Apply migrations (up):
```bash
migrate -path migrations -database "postgres://user:pass@localhost:5432/db?sslmode=disable" up
```

Rollback migrations (down):
```bash
migrate -path migrations -database "postgres://user:pass@localhost:5432/db?sslmode=disable" down 1
```

### Library Usage in Go

It is often useful to run migrations automatically when the application starts.

```go
import (
	"github.com/golang-migrate/migrate/v4"
	_ "github.com/golang-migrate/migrate/v4/database/postgres"
	_ "github.com/golang-migrate/migrate/v4/source/file"
)

func RunMigrations(databaseURL string) error {
	m, err := migrate.New(
		"file://migrations",
		databaseURL,
	)
	if err != nil {
		return err
	}
	defer m.Close()

	if err := m.Up(); err != nil && err != migrate.ErrNoChange {
		return err
	}
	return nil
}

func RollbackMigration(databaseURL string) error {
	m, err := migrate.New(
		"file://migrations",
		databaseURL,
	)
	if err != nil {
		return err
	}
	defer m.Close()

	if err := m.Steps(-1); err != nil && err != migrate.ErrNoChange {
		return err
	}
	return nil
}
```

## Transactions
Handle transactions in the Usecase layer or via a Transaction Manager to maintain layer separation.

```go
func (u *UserUsecase) Process(ctx context.Context) error {
    return u.repo.WithTransaction(ctx, func(txRepo domain.UserRepository) error {
        // ... operations using txRepo
    })
}
```
