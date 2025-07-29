# Solution Steps

1. 1. Scaffold the project directory structure with an 'app' folder for code, and place configuration and dependency files in the root.

2. 2. Define the SQLAlchemy database connection and session handling in 'app/database.py', loading credentials from environment variables and providing a session generator for FastAPI dependencies.

3. 3. Implement the User model in 'app/models.py' with fields 'id', 'name', and 'email', applying a unique constraint to the 'email' field at the database level.

4. 4. Create Pydantic schemas in 'app/schemas.py' for input validation ('UserCreate') and output serialization ('UserOut'), ensuring input emails are valid format.

5. 5. Write CRUD helper functions in 'app/crud.py' for looking up users by email and for creating a new user.

6. 6. Implement the FastAPI app in 'app/main.py': set up database tables, define the '/register' endpoint to accept user registration, check for email uniqueness at the application level (query before insert), and handle database uniqueness errors for robustness.

7. 7. Write a 'Dockerfile' to build the FastAPI service image, installing dependencies from 'requirements.txt' and setting up the command to run the server.

8. 8. Create a 'docker-compose.yml' file to orchestrate both the FastAPI API and a PostgreSQL service with environment variables, persistent volume, and appropriate networking.

9. 9. Add a '.env' file with default environment variables used by the database and the API.

10. 10. Ensure requirements are listed in 'requirements.txt', including FastAPI, Uvicorn, SQLAlchemy, psycopg2-binary, Pydantic, and Python-dotenv.

11. 11. Use 'docker compose build' and 'docker compose up' to run the stack. The registration endpoint will now enforce unique emails both application and database level, responding with 400 Bad Request and a clear error message on duplicate attempts.

