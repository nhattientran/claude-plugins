package main

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/nhattientran/{{args.name}}/internal/infrastructure/config"
)

func main() {
	// Load configuration
	cfg, err := config.LoadConfig(".")
	if err != nil {
		log.Fatalf("failed to load config: %v", err)
	}

	// Initialize logger (standard log for now, can be replaced with zap)
	log.Printf("Starting application in %s mode", cfg.AppEnv)

	// Set gin mode based on environment
	if cfg.AppEnv == "production" {
		gin.SetMode(gin.ReleaseMode)
	}

	r := gin.Default()

	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"status": "up",
			"env":    cfg.AppEnv,
		})
	})

	log.Printf("Server starting on :%s", cfg.Port)
	if err := r.Run(":" + cfg.Port); err != nil {
		log.Fatalf("failed to run server: %v", err)
	}
}
