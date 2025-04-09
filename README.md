# Address Book Application

A Django-based address book with advanced search capabilities.

## Features
- Contact management
- Advanced search
- REST API
- Docker support

## Setup
1. Clone the repository
2. Create `.env` file from `.env.example`
3. Run `docker-compose up --build`
4. Apply migrations: `docker-compose exec web python manage.py migrate`
5. Create admin user: `docker-compose exec web python manage.py createsuperuser`

## Access
- Web interface: http://localhost:8000
- Admin interface: http://localhost:8000/admin
- API: http://localhost:8000/api/contacts/