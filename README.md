
# 🛍️ E-Commerce Product API

A Django REST Framework (DRF) powered backend API for managing **e-commerce products**.  
This project is part of the **ALX Backend Course** assignment and demonstrates modern backend best practices such as authentication, filtering, pagination, and more.

Project Objectives:  
- Design and optimize relational database schemas.  
- Build and document APIs for frontend integration.  
- Enhance backend performance through query optimization and indexing. 
---

## 🎯 Project Goals  
- **CRUD APIs** → Manage products, categories, and users (with authentication).  
- **Filtering, Sorting, Pagination** → Ensure efficient product discovery.  
- **Database Optimization** → High-performance schema design for seamless queries.  

---

## 🛠️ Technologies Used  
- **Django** → Scalable backend framework.  
- **Django REST Framework (DRF)** → API development toolkit.  
- **PostgreSQL** → Relational database for optimized queries.  
- **JWT Authentication** → Secure user authentication.  
- **Swagger** → API documentation and testing.  

---
## 🚀 Key Features  

### 1. CRUD Operations  
- Products & Categories → Create, Read, Update, Delete.  
- User Authentication → JWT-based signup/login.  

### 2. API Features  
- **Filtering & Sorting** → Filter by category, sort by price, etc.  
- **Pagination** → Paginated responses for large datasets.  

### 3. API Documentation  
- Swagger/OpenAPI documentation integrated.  
- Hosted API docs for frontend and developer use.  

---

## 🚀 Features Implemented


### 1. Product Management (CRUD)
- **Create**, **Retrieve**, **Update**, **Delete** products
- Model fields:
  - `name`
  - `description`
  - `price`
  - `category`
  - `created_at`
  - `updated_at`

### 2. API Endpoints for Products
| Method | Endpoint                | Description                      |
|--------|--------------------------|----------------------------------|
| GET    | `/api/products/`         | List all products                |
| POST   | `/api/products/`         | Create a new product             |
| GET    | `/api/products/{id}/`    | Retrieve single product details  |
| PUT    | `/api/products/{id}/`    | Update product details           |
| DELETE | `/api/products/{id}/`    | Delete a product                 |

### 3. Pagination
- **LimitOffsetPagination** implemented
- Clients can control:
  - `?limit=5` → number of items per page
  - `?offset=10` → start position

Example:
```
GET /api/products/?limit=5&offset=10
```

### 4. Sorting
- Products can be sorted by:
  - `price`
  - `name`
  - `created_at`
- Use `?ordering=` parameter:

Examples:
```
GET /api/products/?ordering=price
GET /api/products/?ordering=-created_at   # Descending order
```

### 6. Advanced Filtering
- Filter by multiple fields:
  - `?name=Phone`
  - `?price_min=100&price_max=500`

---
## API Documentation hosted link
- https://ecommerce-app-r82i.onrender.com/api/docs/

---
## Ecommerce App hosted link
- https://ecommerce-app-r82i.onrender.com/api/products/

---

## 👤 Author
**Abdul Jalil Zakaria**  
🔗 Backend Engineer 


