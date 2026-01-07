import sys
import os

def generate_handler(entity_name):
    camel_name = entity_name.capitalize()
    lower_name = entity_name.lower()

    template = f"""package handler

import (
	"net/http"
	"github.com/gin-gonic/gin"
)

type {camel_name}Handler struct {{
	usecase usecase.{camel_name}Usecase
}}

func New{camel_name}Handler(u usecase.{camel_name}Usecase) *{camel_name}Handler {{
	return &{camel_name}Handler{{usecase: u}}
}}

func (h *{camel_name}Handler) Create(c *gin.Context) {{
	var req Create{camel_name}Request
	if err := c.ShouldBindJSON(&req); err != nil {{
		c.JSON(http.StatusBadRequest, gin.H{{"error": err.Error()}})
		return
	}}

	// TODO: Call usecase
	c.JSON(http.StatusCreated, gin.H{{"message": "{lower_name} created"}})
}}

func (h *{camel_name}Handler) GetByID(c *gin.Context) {{
	id := c.Param("id")
	// TODO: Call usecase
	c.JSON(http.StatusOK, gin.H{{"id": id}})
}}

type Create{camel_name}Request struct {{
	Name string `json:"name" binding:"required"`
}}
"""

    filename = f"{lower_name}_handler.go"
    with open(filename, "w") as f:
        f.write(template)
    print(f"Generated {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_handler.py <entity_name>")
    else:
        generate_handler(sys.argv[1])
