# Django Blog Authentication System

## Overview
This authentication system enables users to **register, log in, log out, and manage their profiles** in the Django Blog project.

## Features
- User Registration
- User Login & Logout
- Profile Management
- Secure Password Handling
- CSRF Protection

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/JacklineMacharia/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/django_blog
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
 
4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Authentication Endpoints
| URL Pattern  | View Name  | Description  |
|-------------|-----------|--------------|
| `/register/` | `register_view` | User Registration |
| `/login/` | `login_view` | User Login |
| `/logout/` | `logout_view` | User Logout |
| `/profile/` | `profile_view` | User Profile |

## File Structure
```
Alx_DjangoLearnLab/
├── django_blog/
│   ├── templates/
│   │   ├── blog/
│   │   │   ├── register.html
│   │   │   ├── login.html
│   │   │   ├── profile.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
```

## Testing the Authentication System
1. **Visit the registration page:** `http://127.0.0.1:8000/register/`
2. **Log in:** `http://127.0.0.1:8000/login/`
3. **Access the profile page:** `http://127.0.0.1:8000/profile/`
4. **Logout:** `http://127.0.0.1:8000/logout/`

## Security Measures
- CSRF tokens are included in all forms.
- Passwords are securely hashed using Django’s authentication system.

