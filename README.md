# Real-Time Chat Application 💬

A modern, scalable real-time chat application built with Django and WebSockets. Features user authentication, multiple chat rooms, and a clean modular architecture designed for performance and maintainability.

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=socketdotio&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

## ✨ Features

- **Real-time Messaging**: Instant message delivery using WebSockets
- **User Authentication**: Secure login and registration system
- **Multiple Chat Rooms**: Create and join different chat rooms
- **Responsive Design**: Mobile-friendly interface
- **Modular Architecture**: Clean separation of concerns with dedicated apps
- **Scalable Design**: Built with best practices for future growth

## 🏗️ Architecture

The application follows Django's best practices with a modular structure:

```
Real-Time-Chat/
├── a_core/          # Core application settings and configuration
├── a_home/          # Home page and landing functionality
├── a_rtchat/        # Real-time chat functionality and WebSocket handling
├── a_users/         # User authentication and profile management
├── static/          # Static files (CSS, JS, images)
├── templates/       # HTML templates
└── manage.py        # Django management script
```

### App Responsibilities

- **`a_core`**: Project configuration, settings, and URL routing
- **`a_home`**: Landing page, navigation, and general site functionality
- **`a_rtchat`**: Chat rooms, messaging logic, and WebSocket consumers
- **`a_users`**: User registration, authentication, and profile management

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Django 4.0+
- Redis (for WebSocket channel layer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yousefalimansour/Real-Time-Chat.git
   cd Real-Time-Chat
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Redis**
   - Install Redis on your system
   - Start Redis server:
     ```bash
     redis-server
     ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Visit the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database
DATABASE_URL=sqlite:///db.sqlite3

# Redis (for WebSocket channels)
REDIS_URL=redis://127.0.0.1:6379/1

# Email (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### WebSocket Configuration

The application uses Django Channels for WebSocket support. Make sure Redis is running and properly configured in your settings.

## 📱 Usage

1. **Register/Login**: Create an account or log in with existing credentials
2. **Join/Create Rooms**: Navigate to chat rooms and join existing ones or create new rooms
3. **Start Chatting**: Send messages in real-time with other users
4. **Manage Profile**: Update your profile information and preferences

## 🛠️ Development

### Project Structure Details

```
a_core/
├── settings.py      # Django settings
├── urls.py          # Main URL configuration
├── asgi.py          # ASGI configuration for WebSockets
└── wsgi.py          # WSGI configuration

a_rtchat/
├── models.py        # Chat room and message models
├── views.py         # Chat views
├── consumers.py     # WebSocket consumers
├── routing.py       # WebSocket URL routing
└── templates/       # Chat-specific templates

a_users/
├── models.py        # User profile models
├── views.py         # Authentication views
├── forms.py         # User forms
└── templates/       # User-related templates
```

### Key Technologies

- **Backend**: Django, Django Channels
- **WebSockets**: For real-time communication
- **Database**: SQLite (development) / PostgreSQL (production)
- **Cache/Message Broker**: Redis
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)

## 🔒 Security Features

- CSRF protection on all forms
- Secure WebSocket connections
- User input sanitization
- Session-based authentication
- Environment-based configuration

## 📈 Scalability Considerations

- Modular app structure for easy feature additions
- Redis channel layer for horizontal scaling
- Configurable database backend
- Static file optimization ready
- Docker-ready architecture

## 🚀 Deployment

### Production Deployment

1. **Set environment variables for production**
2. **Configure a production database** (PostgreSQL recommended)
3. **Set up Redis in production**
4. **Configure static file serving**
5. **Use a production WSGI/ASGI server** (Gunicorn + Daphne)
6. **Set up reverse proxy** (Nginx)

### Docker Deployment (Coming Soon)

```bash
docker-compose up --build
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Author

**Yousef Ali Mansour**
- GitHub: [@yousefalimansour](https://github.com/yousefalimansour)
- Email: [your-email@example.com]

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yousefalimansour/Real-Time-Chat/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

## 🔄 Changelog

### v1.0.0 (Current)
- Initial release
- Real-time chat functionality
- User authentication system
- Multiple chat rooms support
- Responsive design

## 🎯 Roadmap

- [ ] Private messaging
- [ ] File sharing
- [ ] Message encryption
- [ ] Mobile app
- [ ] Voice/Video chat
- [ ] Message reactions
- [ ] User presence indicators
- [ ] Chat moderation tools

---

⭐ **Star this repository if you find it helpful!**