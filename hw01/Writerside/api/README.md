# OpenAPI Specification Structure

This directory contains the split OpenAPI specification for the API.

## Structure

- `main.yaml` - Main OpenAPI file with references to all other files
- `paths/` - Directory containing all endpoint definitions
  - `auth.yaml` - Authentication endpoints
  - `customer.yaml` - Customer profile and orders endpoints
  - `products.yaml` - Product management endpoints
  - `shops.yaml` - Shop management endpoints
  - `cart.yaml` - Shopping cart endpoints
  - `order.yaml` - Order management endpoints
  - `delivery.yaml` - Delivery endpoints
  - `payment.yaml` - Payment endpoints
- `schemas/` - Directory containing all data schemas
  - `common.yaml` - Common schemas (Error, etc.)
  - `order.yaml` - Order-related schemas
  - `shop.yaml` - Shop-related schemas
  - `product.yaml` - Product-related schemas

## Usage

To use this specification with Swagger UI or other OpenAPI tools, ensure they support multi-file specifications with `$ref` references.

All paths and schemas are referenced from the main.yaml file using relative paths.
