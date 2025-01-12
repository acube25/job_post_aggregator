# Job Post Aggregator

A FastAPI-based platform to aggregate job posts from Facebook groups.  
This project uses PostgreSQL for database management and JWT-based authentication for user access.

## Features (Updated)
- User registration with hashed passwords.
- JWT-based user login.
- Secure and scalable project structure.
- PostgreSQL integration with SQLAlchemy.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job_post_aggregator.git
   cd job_post_aggregator

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Add environment variables in a .env file:
    ```env
    DATABASE_URL=postgresql://username:password@localhost/job_db
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

# Current Endpoints
## Authentication
- POST /auth/register: User registration
  -  Request Body:
      ```json
      {
          "username": "testuser",
          "email": "test@example.com",
          "password": "testpassword"
      }
      ```
  
  -  Response:
    
      ```json
      {
          "message": "User registered successfully!"
      }
      ```
- `POST /auth/login`: User login
  - Request Body:
    - `username`: testuser    
    - `password`: testpassword
  ### Response:
    ```json
    {
        "access_token": "your_jwt_token",
        "token_type": "bearer"
    }
    ```

## General
- `GET /`: Welcome message
- `GET /test-db/`: Tests database connection

## User Profile Management
- **GET /user/me**: Returns the profile of the logged-in user.
   - Headers: Authorization: Bearer <access_token>
   - Response:
      ```json
      {
          "username": "testuser",
          "email": "test@example.com",
          "id": 1
      }
      ```
  - **Description**: It's provide Users name, mail and auto connected id.
  
## To-Do
- Implement job post aggregation logic.
- Add user roles and permissions.
