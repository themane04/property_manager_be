# 🖥️ Property Manager – Backend

> Django REST API with Djongo + MongoDB, built to support a real estate management dashboard.  
> This is the backend to the [React frontend repo](https://github.com/themane04/property_manager_fe.git).

---

## 🎯 Purpose

This backend powers a property management system allowing internal teams to manage:

- Tenants and rental units
- Contracts and payment records
- Properties and features
- Maintenance requests

It exposes a RESTful API used by the frontend to perform CRUD operations across all models.

---

## 🛠️ Tech Stack

| Tech                        | Purpose                        |
|-----------------------------|--------------------------------|
| Python                      | Primary language               |
| Django                      | Backend web framework          |
| Djongo                      | Connects Django ORM to MongoDB |
| MongoDB                     | Flexible NoSQL database        |
| DRF (Django REST Framework) | REST API layer                 |
| Docker                      | Containerization of services   |

---

## 🐳 Installation (With Docker)

```bash
# Clone the repo
git clone https://github.com/themane04/property_manager_be.git
cd property_manager_be

# Start backend + MongoDB using docker-compose
docker compose up -d

# Stop containers
docker compose down

# Manually connect to the MongoDB container
docker exec -it mongodb-exercise mongosh -u admin -p admin
```

## 📦 Installation (Without Docker)

```bash
# Clone the repo
git clone https://github.com/themane04/property_manager_be.git
cd property_manager_be

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python manage.py runserver
```
