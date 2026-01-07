# Configuration Patterns

## Loading Configuration

Use `viper` for configuration management and `godotenv` to load environment variables from `.env` files during development.

### Centralized Config Struct

Define a centralized `Config` struct that represents the application's configuration. Use tags for mapping from environment variables or config files.

```go
package config

import (
	"log"
	"strings"

	"github.com/joho/godotenv"
	"github.com/spf13/viper"
)

type Config struct {
	App      AppConfig      `mapstructure:"APP"`
	Database DatabaseConfig `mapstructure:"DB"`
	GRPC     GRPCConfig     `mapstructure:"GRPC"`
}

type AppConfig struct {
	Name string `mapstructure:"NAME"`
	Env  string `mapstructure:"ENV"`
}

type DatabaseConfig struct {
	URL string `mapstructure:"URL"`
}

type GRPCConfig struct {
	Port int `mapstructure:"PORT"`
}

// NewConfig loads configuration from environment variables and .env files.
func NewConfig() (*Config, error) {
	// Load .env file if it exists
	_ = godotenv.Load()

	v := viper.New()
	v.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))
	v.AutomaticEnv()

	// Set defaults
	v.SetDefault("APP_ENV", "development")
	v.SetDefault("GRPC_PORT", 50051)

	var cfg Config
	if err := v.Unmarshal(&cfg); err != nil {
		return nil, err
	}

	return &cfg, nil
}
```

## Best Practices

### 1. Avoid Globals
Do not use a global `Config` variable. Load the config in `main.go` and inject it into the layers that need it.

### 2. Dependency Injection
Pass specific configuration sections to the components that need them rather than passing the entire `Config` struct.

```go
// Good: Injecting specific config
func NewDatabase(cfg config.DatabaseConfig) (*gorm.DB, error) {
	return gorm.Open(postgres.Open(cfg.URL), &gorm.Config{})
}

// Avoid: Injecting the entire config
func NewDatabase(cfg *config.Config) (*gorm.DB, error) {
	return gorm.Open(postgres.Open(cfg.Database.URL), &gorm.Config{})
}
```

### 3. Environment Variable Precedence
Ensure that environment variables override values from `.env` files or config files. `viper.AutomaticEnv()` handles this.

### 4. Validation
Validate the configuration at startup to fail fast if required values are missing.

```go
func (c *Config) Validate() error {
    if c.Database.URL == "" {
        return errors.New("database URL is required")
    }
    return nil
}
```
