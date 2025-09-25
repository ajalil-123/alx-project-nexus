
# 🛍️ E-Commerce Product API

A Django REST Framework (DRF) powered backend API for managing **e-commerce products**.  
This project is part of the **ALX Backend Course Nexus** assignment and demonstrates modern backend best practices such as authentication, filtering, pagination, and more.

---

## 🚀 Features Implemented So Far

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

Example:
```
GET /api/products/?category=Electronics&price_min=200&price_max=1000&ordering=-price
```

---

## 📌 Roadmap (Next Features)

- [ ] **JWT Authentication** (Users can register/login and access protected routes)  
- [ ] **User Ownership** (Products tied to the creator account)  
- [ ] **Testing** (Unit + Integration tests)  
- [ ] **Docker Setup** (Optional for deployment readiness)  
- [ ] **CI/CD integration**  

---

## 🛠️ Tech Stack
- **Backend Framework:** Django 5  
- **API Toolkit:** Django REST Framework  
- **Database:** SQLite (dev) → PostgreSQL (production ready)  
- **Auth:** JWT (planned)  

---

## 📖 Installation & Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/ecommerce_product_app.git
   cd ecommerce_product_app
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start server:
   ```bash
   python manage.py runserver
   ```

6. Test API:
   - Open [http://127.0.0.1:8000/api/products/](http://127.0.0.1:8000/api/products/)

---

## 📂 Project Structure
```
ecommerce_product_app/
│── products/
│   ├── models.py       # Product model
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # ViewSets with filtering, sorting, pagination
│   ├── urls.py         # API routes
│── ecommerce_product_app/
│   ├── settings.py     # DRF, installed apps, pagination
│   ├── urls.py         # Project-level routing
│── manage.py
```

---

## 📌 Example API Requests & Responses

### Create Product (POST)
**Request**
```json
POST /api/products/
{
  "name": "iPhone 15",
  "description": "Latest Apple flagship",
  "price": 1200,
  "category": "Electronics"
}
```

**Response**
```json
{
  "id": 1,
  "name": "iPhone 15",
  "description": "Latest Apple flagship",
  "price": 1200,
  "category": "Electronics",
  "created_at": "2025-09-25T12:00:00Z",
  "updated_at": "2025-09-25T12:00:00Z"
}
```

### Get Products with Filters
**Request**
```
GET /api/products/?category=Electronics&price_min=500&ordering=-price&limit=3
```

**Response**
```json
[
  {
    "id": 5,
    "name": "Samsung Galaxy S25",
    "price": 1100,
    "category": "Electronics"
  },
  {
    "id": 3,
    "name": "iPhone 15",
    "price": 1000,
    "category": "Electronics"
  },
  {
    "id": 2,
    "name": "Sony Headphones",
    "price": 600,
    "category": "Electronics"
  }
]
```

---

## 👤 Author
**Abdul Jalil Zakaria**  
🔗 ALX Backend Course Nexus Participant  
