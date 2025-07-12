# Microblog - A Full-Stack Flask Web Application

A modern, feature-rich microblogging platform built with Flask that demonstrates full-stack web development skills including user authentication, database management, and real-time features.

## 📋 Overview

Microblog is a complete social media application where users can create accounts, share posts, follow other users, and interact with content. The application showcases modern web development practices with a clean, responsive design and robust backend functionality.

## ✨ Core Features

### 🔐 User Authentication & Security
- **User Registration & Login**: Secure account creation with email verification
- **Password Reset**: Email-based password recovery system
- **Session Management**: JWT-based authentication with secure session handling
- **Profile Management**: User profiles with customizable avatars and bio

### 📝 Content Management
- **Create Posts**: Rich text posting with markdown support
- **Edit & Delete**: Full CRUD operations on user posts
- **Post Feed**: Chronological feed of posts from followed users
- **Search & Discovery**: Find users and posts through search functionality

### 👥 Social Features
- **Follow System**: Follow/unfollow other users
- **User Profiles**: Detailed user pages with post history
- **Activity Feed**: Personalized content from followed users
- **User Discovery**: Explore and connect with other users

### 🌐 Internationalization
- **Multi-language Support**: Built-in translation system
- **Dynamic Language Switching**: Real-time language changes
- **Localized Content**: Region-specific formatting and content

### 📱 Modern UI/UX
- **Responsive Design**: Mobile-first approach with Bootstrap
- **Real-time Updates**: Dynamic content without page refreshes
- **Clean Interface**: Intuitive navigation and modern styling
- **Accessibility**: WCAG compliant design patterns

## 🎯 What I Learned

### Backend Development
- **Flask Framework**: Mastered Flask's application factory pattern, blueprints, and routing system
- **Database Design**: Designed and implemented relational database schemas using SQLAlchemy ORM
- **Authentication Systems**: Built secure JWT-based authentication with password hashing and session management
- **API Development**: Created RESTful endpoints with proper error handling and validation
- **Email Integration**: Implemented transactional email systems for user verification and password resets

### Frontend Development
- **Jinja2 Templating**: Leveraged Flask's templating engine for dynamic content rendering
- **Form Handling**: Built complex forms with CSRF protection and client-side validation
- **Responsive Design**: Created mobile-responsive layouts using Bootstrap and custom CSS
- **JavaScript Integration**: Added interactive features with vanilla JavaScript and AJAX

### DevOps & Deployment
- **Environment Management**: Configured development and production environments
- **Database Migrations**: Implemented Alembic for database schema versioning
- **Error Handling**: Built comprehensive error handling and logging systems
- **Security Best Practices**: Implemented security headers, input validation, and XSS protection

### Software Architecture
- **Blueprint Architecture**: Organized code using Flask blueprints for modularity
- **Configuration Management**: Implemented environment-based configuration system
- **Testing**: Wrote unit tests and integration tests for critical functionality
- **Code Organization**: Maintained clean, maintainable code with proper separation of concerns

## 🛠️ Tech Stack

### Backend
- **Python 3.11+**: Core programming language
- **Flask 2.3+**: Web framework with blueprints and extensions
- **SQLAlchemy 2.0+**: ORM for database operations
- **Alembic**: Database migration tool
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and CSRF protection
- **PyJWT**: JSON Web Token implementation
- **Flask-Mail**: Email functionality
- **Flask-Babel**: Internationalization support

### Database
- **SQLite**: Development database (easily configurable for PostgreSQL/MySQL in production)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Styling with Bootstrap 5 and custom CSS
- **JavaScript (ES6+)**: Client-side interactivity
- **Jinja2**: Server-side templating engine

### Development Tools
- **Git**: Version control
- **Virtual Environment**: Python dependency isolation
- **Flask CLI**: Development server and commands
- **VS Code**: Development environment

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/microblog.git
   cd microblog
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize the database**
   ```bash
   flask db upgrade
   ```

6. **Run the application**
   ```bash
   flask run
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Environment Variables
Create a `.env` file with the following variables:
```env
FLASK_APP=microblog.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## 🏗️ Project Structure

```
microblog/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── forms.py             # Form definitions
│   ├── routes.py            # Main application routes
│   ├── auth/                # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── routes.py        # Auth routes
│   │   └── forms.py         # Auth forms
│   ├── templates/           # Jinja2 templates
│   │   ├── base.html        # Base template
│   │   ├── index.html       # Homepage
│   │   ├── user.html        # User profile
│   │   └── auth/            # Auth templates
│   └── static/              # Static files (CSS, JS, images)
├── migrations/              # Database migrations
├── tests/                   # Test suite
├── microblog.py            # Application entry point
├── config.py               # Configuration settings
└── requirements.txt        # Python dependencies
```

## 🧪 Testing

Run the test suite to ensure everything is working correctly:
```bash
python -m pytest tests/
```

## 🤝 Contributing

This is a personal project showcasing my skills, but I welcome feedback and suggestions for improvement.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **GitHub**: [@William-Liangg](https://github.com/William-Liangg)
- **LinkedIn**: [William Liang](https://linkedin.com/in/william-liang-5007552a9/)
- **Portfolio**: https://william-liangg.github.io/portfolio/

---

*Built with ❤️ using Flask and modern web technologies* 
