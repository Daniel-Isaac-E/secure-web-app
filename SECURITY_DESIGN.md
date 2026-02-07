# Security Design Explanation

## Password Security
Passwords are never stored in plaintext. The application uses bcrypt hashing with salting to protect user credentials even if the database is compromised.

## Authentication & Authorization
Users must authenticate before accessing protected resources. Authorization checks ensure only admins can access restricted routes.

## Input Validation
All user inputs are validated server-side. Parameterized queries are used to prevent SQL injection attacks.

## Session Security
Session-based authentication is implemented. Sessions are cleared on logout to reduce session hijacking risks.

## Access Control
Each protected route verifies the user’s role before granting access, ensuring principle of least privilege.