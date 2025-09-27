
# 🛍️ E-Commerce Product API

A Django REST Framework (DRF) powered backend API for managing **e-commerce products**.  
This project is part of the **ALX Backend Course** assignment and demonstrates modern backend best practices such as authentication, filtering, pagination, and more.

---

## 🚀 Features Implemented

### 1. Project Setup
- Django 5 + Django REST Framework
- Structured app: `products` for product management
- Configured `settings.py` for DRF defaults

### 2. Product Management (CRUD)
- **Create**, **Retrieve**, **Update**, **Delete** products
- Model fields:
  - `name`
  - `description`
  - `price`
  - `category`
  - `created_at`
  - `updated_at`

### 3. API Endpoints
| Method | Endpoint                | Description                      |
|--------|--------------------------|----------------------------------|
| GET    | `/api/products/`         | List all products                |
| POST   | `/api/products/`         | Create a new product             |
| GET    | `/api/products/{id}/`    | Retrieve single product details  |
| PUT    | `/api/products/{id}/`    | Update product details           |
| DELETE | `/api/products/{id}/`    | Delete a product                 |

### 4. Pagination
- **LimitOffsetPagination** implemented
- Clients can control:
  - `?limit=5` → number of items per page
  - `?offset=10` → start position

Example:
```
GET /api/products/?limit=5&offset=10
```

### 5. Sorting
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
  - `?category=Electronics`
  - `?price_min=100&price_max=500`
- Combine filters:


---

## 🛠️ Tech Stack
- **Backend Framework:** Django 5  
- **API Toolkit:** Django REST Framework  
- **Database:** SQLite (dev)  
- **Auth:** JWT (planned)  

---
## API Documentation hosted link
- https://ecommerce-app-r82i.onrender.com/api/docs/

---

## 👤 Author
**Abdul Jalil Zakaria**  
🔗 Backend Engineer 

