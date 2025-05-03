# MiniMart Project 🛒

A simple Django REST API project for managing Customers, Products, and Orders with full CRUD functionality. Built using Django REST Framework and deployed on AWS.

## Features
- CRUD operations for Customers, Products, and Orders
- Clean project structure following Django best practices
- RESTful APIs with serializers and validations
- Environment-based settings structure
- Hosted on AWS EC2 with RDS
- Postman documentation for all endpoints

## Tech Stack
- Python, Django, Django REST Framework
- SQLite (local) / AWS RDS (production)
- AWS EC2 for deployment
- Postman for API documentation

## Run Project Locally
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver