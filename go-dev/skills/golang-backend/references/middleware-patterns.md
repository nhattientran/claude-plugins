# Middleware Patterns

## Authentication (JWT)
Extract token from `Authorization: Bearer <token>` header.

```go
func AuthMiddleware(secret string) gin.HandlerFunc {
    return func(c *gin.Context) {
        authHeader := c.GetHeader("Authorization")
        // ... parse and validate JWT
        c.Set("user_id", claims.UserID)
        c.Next()
    }
}
```

## CORS
Configure specific origins, methods, and headers.

```go
func CORSMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
        if c.Request.Method == "OPTIONS" {
            c.AbortWithStatus(204)
            return
        }
        c.Next()
    }
}
```

## Logging & Recovery
Use structured logging (Zap/Slog).

```go
func Logger(logger *slog.Logger) gin.HandlerFunc {
    return func(c *gin.Context) {
        start := time.Now()
        c.Next()
        logger.Info("request",
            "method", c.Request.Method,
            "path", c.Request.URL.Path,
            "status", c.Writer.Status(),
            "latency", time.Since(start),
        )
    }
}
```
