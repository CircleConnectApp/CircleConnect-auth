# API Documentation

## Authorization Endpoints

- http://localhost:8000 

### GET /auth/login

Redirects the user to Google OAuth login.

- **Query Parameters:** None
- **Response:**
    - A URL to redirect the user to Google login.

---

### GET /auth/callback

Callback URL where Google OAuth sends the authorization code.

- **Query Parameters:**
    - `code` (string) - The authorization code returned by Google.
- **Response:**
    - A JWT token (`access_token`) which can be used for authenticated requests.