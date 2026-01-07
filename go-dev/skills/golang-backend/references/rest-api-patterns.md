# REST API Patterns

## Gin Framework Pattern

### Handler Implementation
Follow Uber Style Guide: avoid global state, use receivers.

```go
type UserHandler struct {
    usecase usecase.UserUsecase
}

func (h *UserHandler) Create(c *gin.Context) {
    var req CreateUserRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    // ... call usecase
}
```

## Validation
Use `validator` tags in structs:

```go
type CreateUserRequest struct {
    Email    string `json:"email" binding:"required,email"`
    Password string `json:"password" binding:"required,min=8"`
}
```

## Pagination & Filtering (camelCase)

**IMPORTANT**: Use camelCase for all query parameters and JSON response fields.

### Pagination Request
```go
type PaginationRequest struct {
    Page     int    `form:"page" binding:"min=1"`
    PageSize int    `form:"pageSize" binding:"min=1,max=100"`
    SortBy   string `form:"sortBy"`
    SortDir  string `form:"sortDir" binding:"omitempty,oneof=asc desc"`
}

// Default values
func (p *PaginationRequest) SetDefaults() {
    if p.Page == 0 {
        p.Page = 1
    }
    if p.PageSize == 0 {
        p.PageSize = 10
    }
}
```

### Filter Request
```go
type FilterRequest struct {
    SearchQuery string `form:"searchQuery"`
    Status      string `form:"status"`
    CreatedFrom string `form:"createdFrom"` // ISO8601 format
    CreatedTo   string `form:"createdTo"`   // ISO8601 format
    CategoryID  string `form:"categoryId"`
    IsActive    *bool  `form:"isActive"`
}
```

### Paginated Response (camelCase)
```go
type PaginatedResponse[T any] struct {
    Data       []T   `json:"data"`
    Page       int   `json:"page"`
    PageSize   int   `json:"pageSize"`
    TotalItems int64 `json:"totalItems"`
    TotalPages int   `json:"totalPages"`
    HasNext    bool  `json:"hasNext"`
    HasPrev    bool  `json:"hasPrev"`
}

func NewPaginatedResponse[T any](data []T, page, pageSize int, total int64) PaginatedResponse[T] {
    totalPages := int((total + int64(pageSize) - 1) / int64(pageSize))
    return PaginatedResponse[T]{
        Data:       data,
        Page:       page,
        PageSize:   pageSize,
        TotalItems: total,
        TotalPages: totalPages,
        HasNext:    page < totalPages,
        HasPrev:    page > 1,
    }
}
```

### Example Usage
```go
// GET /products?page=1&pageSize=10&sortBy=createdAt&sortDir=desc&searchQuery=phone&categoryId=123
func (h *ProductHandler) List(c *gin.Context) {
    var pagination PaginationRequest
    var filter FilterRequest

    if err := c.ShouldBindQuery(&pagination); err != nil {
        HandleError(c, err)
        return
    }
    pagination.SetDefaults()

    if err := c.ShouldBindQuery(&filter); err != nil {
        HandleError(c, err)
        return
    }

    products, total, err := h.usecase.List(c.Request.Context(), pagination, filter)
    if err != nil {
        HandleError(c, err)
        return
    }

    c.JSON(http.StatusOK, NewPaginatedResponse(products, pagination.Page, pagination.PageSize, total))
}
```

### Query Parameter Naming Convention
| Purpose | Parameter Name (camelCase) |
|---------|---------------------------|
| Current page | `page` |
| Items per page | `pageSize` |
| Sort field | `sortBy` |
| Sort direction | `sortDir` |
| Text search | `searchQuery` |
| Date range start | `createdFrom` / `updatedFrom` |
| Date range end | `createdTo` / `updatedTo` |
| Foreign key filter | `categoryId`, `userId`, `orderId` |
| Boolean filter | `isActive`, `isPublished` |
| Status filter | `status` |

## Error Handling
Centralize error mapping:

```go
type ErrorResponse struct {
    Code    string `json:"code"`
    Message string `json:"message"`
    Details any    `json:"details,omitempty"`
}

func HandleError(c *gin.Context, err error) {
    switch {
    case errors.Is(err, domain.ErrNotFound):
        c.JSON(http.StatusNotFound, ErrorResponse{Code: "NOT_FOUND", Message: "Resource not found"})
    case errors.Is(err, domain.ErrValidation):
        c.JSON(http.StatusBadRequest, ErrorResponse{Code: "VALIDATION_ERROR", Message: err.Error()})
    case errors.Is(err, domain.ErrUnauthorized):
        c.JSON(http.StatusUnauthorized, ErrorResponse{Code: "UNAUTHORIZED", Message: "Authentication required"})
    case errors.Is(err, domain.ErrForbidden):
        c.JSON(http.StatusForbidden, ErrorResponse{Code: "FORBIDDEN", Message: "Access denied"})
    default:
        c.JSON(http.StatusInternalServerError, ErrorResponse{Code: "INTERNAL_ERROR", Message: "Internal server error"})
    }
}
```

## Response Format
Standardize responses with camelCase:

```go
type Response struct {
    Data    any    `json:"data,omitempty"`
    Error   string `json:"error,omitempty"`
    Message string `json:"message,omitempty"`
}

type SingleResponse[T any] struct {
    Data T `json:"data"`
}
```

## RESTful Conventions
- `GET /resources` - List with pagination (`?page=1&pageSize=10`)
- `GET /resources/:id` - Get single resource
- `POST /resources` - Create resource
- `PUT /resources/:id` - Full update
- `PATCH /resources/:id` - Partial update
- `DELETE /resources/:id` - Delete resource
