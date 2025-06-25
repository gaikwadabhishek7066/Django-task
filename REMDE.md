# 🛠️ Django Backend Assignment

This is a small backend project built with **Django**, **Django REST Framework (DRF)**, **JWT Authentication**, **Celery with Redis**, and **Telegram Bot Integration**. 

---

##  Features

- Django REST Framework with JWT authentication
- Public and Protected API endpoints
- Django admin login
- Celery + Redis for background tasks
- Sends welcome email after user registration
- Telegram bot integration (/start command saves username)
- Production-ready setup with `.env` configuration
- Clean code structure and GitHub version control

---


python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

---

#  Install Dependencies
pip install -r requirements.txt