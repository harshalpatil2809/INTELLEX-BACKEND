# 🧠 Intellex Backend

> A powerful AI-powered chat application built with Django REST Framework and Groq API

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.3-darkgreen?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running the Project](#-running-the-project)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Docker Setup](#-docker-setup)
- [Contributing](#-contributing)

---

## 🎯 Overview

**Intellex Backend** is a sophisticated RESTful API backend for an AI-powered chat application. It seamlessly integrates with the Groq API to provide intelligent, real-time AI responses while maintaining secure user authentication and conversation management.

Built with modern Django best practices, it supports JWT-based authentication, social login via Google, and provides a scalable architecture for multi-user chat conversations.

---

## ✨ Features

- 🔐 **User Authentication**
  - User registration and login
  - JWT token-based authentication
  - Token refresh mechanism
  - Secure logout with token blacklisting
  - Social authentication (Google OAuth)

- 💬 **Chat Management**
  - Create multiple conversations
  - Send and receive messages
  - Maintain conversation history
  - Real-time AI responses via Groq API

- 🤖 **AI Integration**
  - Powered by Groq API (GPT-OSS-120B model)
  - Intelligent message processing
  - Context-aware responses

- 🔒 **Security**
  - CORS enabled
  - CSRF protection
  - Environment-based configuration
  - Django admin interface

- 🐳 **DevOps Ready**
  - Docker & Docker Compose support
  - PostgreSQL database integration
  - Production-ready setup

---

## 🛠 Tech Stack

### Backend Framework
- **Django 6.0.3** - Web framework
- **Django REST Framework** - API development
- **djangorestframework-simplejwt** - JWT authentication
- **dj-rest-auth** - Authentication endpoints

### Database
- **PostgreSQL 15** - Primary database
- **SQLite** - Development database

### AI & APIs
- **Groq SDK** - AI model integration
- **OpenAI GPT-OSS-120B** - Language model

### Authentication & Authorization
- **Django AllAuth** - User authentication
- **Google OAuth 2.0** - Social login
- **CORS Headers** - Cross-origin requests

### Containerization
- **Docker** - Container platform
- **Docker Compose** - Container orchestration

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+**
- **PostgreSQL 15+** (if not using Docker)
- **Docker & Docker Compose** (optional but recommended)
- **pip** or **conda** (Python package manager)
- **Git**

---

## 📥 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Intellex-backend.git
cd Intellex-backend/backend
```

### Using Virtual Environment (without Docker)

#### 1. Create a Virtual Environment
```bash
python -m venv venv
```

#### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Create Environment Variables
```bash
cp .env.example .env
```

Edit `.env` and configure:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
GROQ_API_KEY=your-groq-api-key
DATABASE_URL=postgresql://user:password@localhost:5432/intellex_db
```

#### 5. Run Migrations
```bash
python manage.py migrate
```

#### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

#### 7. Start Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

---

## 🐳 Docker Setup

### Using Docker Compose (Recommended)

#### 1. Ensure Docker is Installed and Running

#### 2. Create Environment File
```bash
cp .env.example .env
```

Configure the `.env` file with your settings.

#### 3. Build and Run Containers
```bash
docker-compose up -d
```

This will:
- Start PostgreSQL database (port 5432)
- Start Django backend (port 8000)
- Create necessary volumes for data persistence

#### 4. Run Migrations in Docker
```bash
docker-compose exec backend python manage.py migrate
```

#### 5. Create Superuser in Docker
```bash
docker-compose exec backend python manage.py createsuperuser
```

#### 6. Stop Containers
```bash
docker-compose down
```

#### 7. View Logs
```bash
docker-compose logs -f backend
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Django Settings
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=intellex_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432

# Groq API Configuration
GROQ_API_KEY=your-groq-api-key

# JWT Configuration
JWT_SECRET=your-jwt-secret
JWT_EXPIRATION_HOURS=24

# Email Configuration (Optional)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Django Settings

Key settings are configured in `backend/settings.py`:

- **Installed Apps**: Django core + DRF + AllAuth + CORS
- **Database**: PostgreSQL (production) or SQLite (development)
- **Authentication**: JWT + Session authentication
- **CORS**: Enabled for all origins (configure as needed)

---

## 🚀 Running the Project

### Development Mode

```bash
# Using virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows
python manage.py runserver

# Using Docker
docker-compose up
```

### Production Mode

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Start server with Gunicorn (recommended)
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
```

---

## 📡 API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/api/auth/register/` | Register a new user | ❌ |
| POST | `/api/auth/login/` | Login user | ❌ |
| POST | `/api/auth/logout/` | Logout user | ✅ |
| POST | `/api/auth/refresh/` | Refresh JWT token | ❌ |
| GET | `/api/auth/user/` | Get current user info | ✅ |

### Chat Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/api/chat/create/` | Create new conversation | ✅ |
| POST | `/api/chat/send/` | Send message & get AI response | ✅ |
| GET | `/api/chat/list/` | Get all conversations | ✅ |
| GET | `/api/chat/messages/<id>/` | Get messages from conversation | ✅ |

### Admin Panel

| Endpoint | Description |
|----------|-------------|
| `/admin/` | Django admin interface |
| `/accounts/` | AllAuth authentication URLs |

---

## 📂 Project Structure

```
Intellex-backend/
├── backend/                    # Django project settings
│   ├── __init__.py
│   ├── asgi.py                # ASGI configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
│
├── chat/                       # Chat application
│   ├── __init__.py
│   ├── models.py              # Conversation & Message models
│   ├── views.py               # Chat API views
│   ├── urls.py                # Chat URL patterns
│   ├── admin.py               # Admin configuration
│   ├── serializers.py         # DRF serializers
│   └── migrations/            # Database migrations
│
├── users/                      # User management application
│   ├── __init__.py
│   ├── models.py              # Custom User model
│   ├── views.py               # Auth API views
│   ├── serializers.py         # Auth serializers
│   ├── urls.py                # User URL patterns
│   ├── adapters.py            # Social auth adapters
│   ├── admin.py               # Admin configuration
│   └── migrations/            # Database migrations
│
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose configuration
├── db.sqlite3                  # SQLite database (development)
└── Readme.md                   # This file

```

---

## 📚 API Usage Examples

### 1. Register a New User

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

**Response:**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  },
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 2. Login

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'
```

### 3. Create a New Chat

```bash
curl -X POST http://localhost:8000/api/chat/create/ \
  -H "Authorization: Bearer <your-access-token>" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "id": 1
}
```

### 4. Send a Message

```bash
curl -X POST http://localhost:8000/api/chat/send/ \
  -H "Authorization: Bearer <your-access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": 1,
    "message": "What is artificial intelligence?"
  }'
```

**Response:**
```json
{
  "reply": "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines..."
}
```

### 5. Get All Conversations

```bash
curl -X GET http://localhost:8000/api/chat/list/ \
  -H "Authorization: Bearer <your-access-token>"
```

---

## 🔧 Troubleshooting

### Port Already in Use

```bash
# Find and kill process using port 8000
# Windows
netstat -ano | findstr :8000

# macOS/Linux
lsof -i :8000
kill -9 <PID>
```

### Database Connection Issues

```bash
# Check PostgreSQL is running
# Windows
Get-Service PostgreSQL

# macOS
brew services list | grep postgresql

# Linux
sudo systemctl status postgresql
```

### Groq API Key Issues

- Ensure `GROQ_API_KEY` is set in `.env`
- Verify the API key is valid at [Groq Console](https://console.groq.com/)
- Check API rate limits

### Migration Issues

```bash
# Reset database migrations (development only)
python manage.py migrate --fake chat zero
python manage.py migrate
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python
- Write descriptive commit messages
- Add tests for new features
- Update documentation accordingly
- Use Django best practices

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name/Organization**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Groq API Documentation](https://console.groq.com/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## 📞 Support

For support, email your-email@example.com or open an issue on GitHub.

---

<div align="center">

**Made with ❤️ by the Intellex Team**

⭐ Please star this repository if you find it helpful!

</div>
