# Secure Web Application & Threat Hardening

## Project Overview
This project is a secure web application developed to demonstrate core cyber security principles such as authentication, authorization, password security, and threat mitigation. The application focuses on secure logic rather than UI design.

## Core Features
- User Registration and Login
- Role-Based Access Control (User / Admin)
- Secure Session Management
- Admin-Only Restricted Pages

## Security Features Implemented
### Authentication & Authorization
- Secure login and signup flow
- Role-based access control to restrict admin resources

### Password Hashing & Policy
- Passwords are hashed using bcrypt
- Strong password policy enforced:
  - Minimum 8 characters
  - Uppercase, lowercase, number, and special character required

### Input Validation & Sanitization
- Server-side input validation
- Parameterized SQL queries to prevent SQL Injection
- Output rendered safely to prevent XSS attacks

### Session Handling & Access Control
- Secure session-based authentication
- Session cleared on logout
- Unauthorized access blocked

## Application Flow
1. User signs up with strong password
2. Password is hashed and stored securely
3. User logs in and session is created
4. Access is granted based on user role
5. Unauthorized access attempts are blocked
6. Session is destroyed on logout

## Threats Mitigated
- SQL Injection
- Cross-Site Scripting (XSS)
- Credential theft
- Unauthorized access
- Session hijacking

## Screenshots
(Add screenshots of signup, login, dashboard, unauthorized access, and admin panel)

## How to Run
```bash
pip install -r requirements.txt
python app.py
