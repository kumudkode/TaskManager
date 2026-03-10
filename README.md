# Task Management Application

## Project Overview
A web-based Task Management application focusing on CRUD operations and robust search capabilities. Built using Python, Flask, SQLite, and Bootstrap. This application helps users efficiently create, store, and manage their tasks.

## Features
- **Create**: Add new tasks with title, description, due date, status, assigned by, and remarks.
- **Read**: View all tasks presented in a clean dashboard with important details readily visible.
- **Update**: Edit existing tasks and keep track of who updated them and when.
- **Delete**: Remove unneeded tasks permanently with confirmation.
- **Search**: Robust filtering system to find tasks by title and status.

## Tech Stack
**Frontend:**
- HTML
- CSS
- Bootstrap
- Jinja2

**Backend:**
- Python
- Flask
- SQLite
- Flask-SQLAlchemy

## Database Explanation
The database uses an SQLite file `database.db` exposed via **Flask-SQLAlchemy**. 

The central model is the `Task` with the following fields:
- `id`: Primary key for the task.
- `title`: The title of the task (Required).
- `description`: Detailed information about the task.
- `due_date`: When the task is expected to be completed.
- `status`: Current stage of the task (Pending, In Progress, Completed).
- `remarks`: Additional notes or comments.
- `created_on`: Timestamp recording when the task was initially created.
- `updated_on`: Automatically updating timestamp for the youngest modification.
- `created_by`: Name or ID of the user who originated the task.
- `updated_by`: Name or ID of the user who last modified the task.

## Setup Steps
1. Make sure Python is installed.
2. Install the required dependencies:
```bash
pip install flask flask-sqlalchemy
```
3. Run the application:
```bash
python app.py
```
4. Access the application in your browser at `http://localhost:5000/`.
