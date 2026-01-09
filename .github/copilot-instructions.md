# Copilot Instructions for POO-Python-ORM-et-FASTAPI

## Project Overview
This project is structured around a FastAPI application, utilizing an ORM for database interactions. The architecture is modular, with clear separations between different components such as models, repositories, services, and routes.

## Key Components
- **`src/`**: Contains the main application code.
  - **`main.py`**: The entry point for the FastAPI application.
  - **`models/`**: Defines the data models used in the application.
  - **`repositories/`**: Contains data access logic, interacting with the database.
  - **`services/`**: Business logic layer, coordinating between models and repositories.
  - **`routes/`**: Defines the API endpoints and their corresponding handlers.
  - **`utils/`**: Utility functions and helpers.

## Developer Workflows
- **Running the Application**: Use `uvicorn` to run the FastAPI application.
  ```bash
  uvicorn src.main:app --reload
  ```
- **Testing**: Tests are located in the `tests/` directory. Use `pytest` to run the tests.
  ```bash
  pytest tests/
  ```

## Project Conventions
- Follow PEP 8 for Python code style.
- Use type hints for function signatures to improve code clarity and assist with static analysis.

## Integration Points
- The application integrates with a database through the ORM defined in the `models/` and `repositories/` directories.
- API routes defined in `routes/` communicate with the services in `services/`.

## External Dependencies
- Ensure all dependencies are listed in `requirements.txt`. Use `pip install -r requirements.txt` to install them.

## Example Patterns
- **Service Pattern**: Each service should encapsulate business logic and interact with one or more repositories.
- **Repository Pattern**: Each repository should handle data access for a specific model.
