# Flask API Project

## Overview
This project is a Flask API that provides user authentication and management features using a MongoDB database. It includes endpoints for user login, user creation, retrieving user information, deleting a user, and a password recovery feature.

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-api-project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the application:**
   Update the `config.py` file with your MongoDB connection details and any other necessary configurations.

5. **Run the application:**
   ```
   flask run
   ```

## API Endpoints
- **User Creation:** `POST /api/users`
- **User Login:** `POST /api/auth/login`
- **Retrieve User Information:** `GET /api/users/<user_id>`
- **Delete User:** `DELETE /api/users/<user_id>`
- **Password Recovery:** `POST /api/auth/recover`

## License
This project is licensed under the MIT License.