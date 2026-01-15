# Django CRM - Content Management System

A Django-based Customer Relationship Management (CRM) system for managing customer records with user authentication and record management capabilities.

## Project Overview

This is a Django web application that provides a platform for managing customer information. Users can register, log in, view, add, update, and delete customer records. The system includes user authentication and authorization to ensure data security.

## Features

- **User Authentication**: Register and login functionality for secure access
- **Customer Record Management**: Create, read, update, and delete (CRUD) customer records
- **User Authorization**: Only authenticated users can access and manage records
- **Responsive Templates**: HTML templates for all major operations
- **Database Support**: MySQL backend for persistent data storage
- **Form Validation**: Django forms with built-in validation for user and record data

## Technology Stack

- **Framework**: Django 5.0+
- **Database**: MySQL
- **Backend**: Python 3.10+
- **Package Manager**: UV
- **Additional Libraries**:
  - djangorestframework
  - python-dotenv
  - mysqlclient
  - mysql-connector-python

## Project Structure

```
.
├── CRM/                          # Main Django app
│   ├── migrations/               # Database migrations
│   ├── models.py                 # Database models (Record model)
│   ├── views.py                  # View functions for handling requests
│   ├── forms.py                  # Django forms (Login, Registration, Record)
│   ├── urls.py                   # URL routing
│   ├── admin.py                  # Django admin configuration
│   ├── apps.py                   # App configuration
│   └── tests.py                  # Unit tests
├── Name/                         # Django project configuration
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI application
│   └── asgi.py                   # ASGI application
├── templates/                    # HTML templates
│   ├── base.html                 # Base template
│   ├── home.html                 # Home page with record listing
│   ├── register.html             # User registration page
│   ├── record.html               # Individual record detail view
│   ├── add_record.html           # Add new record form
│   ├── update_record.html        # Update existing record form
│   └── navbar.html               # Navigation bar component
├── manage.py                     # Django management script
├── create_db.py                  # Database creation script
├── pyproject.toml                # Project dependencies and metadata
└── README.md                     # This file
```

## Database Models

### Record Model

Represents a customer record with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| first_name | CharField | Customer's first name (max 50 chars) |
| last_name | CharField | Customer's last name (max 50 chars) |
| email | EmailField | Unique email address |
| phone_number | CharField | Phone number (optional, max 15 chars) |
| city | CharField | City (optional, max 100 chars) |
| state | CharField | State/Province (optional, max 100 chars) |
| country | CharField | Country (optional, max 100 chars) |
| zip_code | CharField | Postal/ZIP code (optional, max 20 chars) |
| created_at | DateTimeField | Auto-populated creation timestamp |
| updated_at | DateTimeField | Auto-updated modification timestamp |

## URL Routes

| Route | View | Description |
|-------|------|-------------|
| `/` | home | Display all records and login form |
| `/login/` | login_view | Display login form |
| `/logout/` | logout_view | Log out user |
| `/register/` | register_view | User registration page |
| `/record/<pk>/` | customer_record | View individual customer record |
| `/delete_record/<pk>/` | delete_record | Delete a customer record |
| `/add_record/` | add_record | Add new customer record |
| `/update_record/<pk>/` | update_record | Update existing customer record |

## Installation & Setup

### Prerequisites

- Python 3.10 or higher
- MySQL server running
- UV package manager installed

### Step 1: Clone the Repository

```bash
cd c:\Users\pramish\Desktop\content_management_system\Name
```

### Step 2: Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
uv pip install -e .
```

Or with pip:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Database

Update the database credentials in [Name/settings.py](Name/settings.py):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Step 5: Run Migrations

```bash
python manage.py migrate
```

### Step 6: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

1. **Register**: Navigate to `/register/` to create a new account
2. **Login**: Use credentials on the home page or navigate to `/login/`
3. **View Records**: Once logged in, view all customer records on the home page
4. **Add Record**: Click "Add Record" button to create a new customer entry
5. **View Detail**: Click on a customer name to see full details
6. **Update Record**: Edit customer information using the update form
7. **Delete Record**: Remove a customer record (authentication required)
8. **Logout**: Click logout to end your session

## Forms

### LoginForm
- Username (required)
- Password (required, minimum 5 characters)

### RegistrationForm
- Username (required, unique)
- Email (required, unique)
- Password (required)
- Confirm Password (required)

### RecordForm
- First Name (required)
- Last Name (required)
- Email (required, unique)
- Phone Number (required)
- City (required)
- Country (required)
- State (required)
- ZIP Code (required)

## Security Features

- User authentication with Django's built-in auth system
- Authorization checks for sensitive operations (delete, update)
- CSRF protection
- Password hashing
- Email uniqueness validation

## Development

### Running Tests

```bash
pytest
```

### Code Quality Tools

- **Ruff**: Linting
- **Black**: Code formatting

### Format Code

```bash
black .
```

### Lint Code

```bash
ruff .
```

## Future Enhancements

- Email verification for user registration
- Record search and filtering functionality
- Pagination for large record lists
- User profile management
- Export records to CSV/PDF
- Advanced reporting features
- REST API endpoints with Django REST Framework
- Deployment configuration for production

## Requirements

See [pyproject.toml](pyproject.toml) for complete dependency list:

```
Django>=5
djangorestframework
python-dotenv
mysqlclient
mysql-connector-python
```

## Notes

- **DEBUG MODE**: Currently set to `True` for development. Change to `False` for production.
- **SECRET KEY**: The current secret key is exposed and should be changed before production deployment.
- **ALLOWED_HOSTS**: Currently empty. Add appropriate hosts for production.
- **Database**: Ensure MySQL is running and the `demo` database exists before running migrations.

## License

This project is provided as-is for educational and development purposes.

## Contact

For questions or issues, please refer to the project repository or contact the development team.
