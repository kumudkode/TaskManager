# newReadme.md

## 2.1.3.1. Overview of what is being built
This is a robust, web-based **Task Management Application** built to efficiently create, store, and manage user tasks focusing on continuous CRUD (Create, Read, Update, Delete) operations and dynamic search capabilities. Python, Flask, SQLite, and Bootstrap are used as the core tech stack.

## 2.1.3.2. Explanation of DB Design
The application uses **SQLite** combined with **Flask-SQLAlchemy** as its underlying database architecture to securely store data interactively.

### 2.1.3.2.1. ER Diagram

```mermaiderDiagram
    Task {
        Integer id PK
        String title
        Text description
        String due_date
        String status
        Text remarks
        DateTime created_on
        DateTime updated_on
        String created_by
        String updated_by
    }
```

### 2.1.3.2.2. Data Dictionary

| Field | Data Type | Properties | Description |
|-------|-----------|------------|-------------|
| `id` | Integer | Primary Key | Unique identifier for each task. |
| `title` | String(255) | Not Null | The main headline or name of the task. |
| `description` | Text | Nullable | A detailed background elaboration about the task. |
| `due_date` | String(10) | Nullable | Target completion date formatted as YYYY-MM-DD. |
| `status` | String(50) | Not Null, Default: 'Pending' | Current stage (e.g., Pending, In Progress, Completed). |
| `remarks` | Text | Nullable | Additional context or comments. |
| `created_on` | DateTime | Default: `datetime.utcnow` | Auto-recorded timestamp of task creation. |
| `updated_on` | DateTime | Default: `datetime.utcnow` | Auto-recorded timestamp capturing recent modification. |
| `created_by` | String(100) | Nullable | The user who originally created the item. |
| `updated_by` | String(100) | Nullable | The user who last modified the item. |

### 2.1.3.2.3. Documentation of Indexes used
- **Primary Key Index on `id`:** The relational database automatically creates a unique index on the primary key `id` column directly to efficiently fetch, update, and sort records by their primary identifier. 
- *No additional custom or composite indexing rules were defined.* 

### 2.1.3.2.4. Code First vs DB First approach
A **Code First** (Model First/Object Relational Mapping) approach was utilized through Flask-SQLAlchemy. 
**Why?**
We define database schemas dynamically using Python classes (e.g., `class Task(db.Model)`) instead of writing raw SQL structural component scripts manually. The ORM mechanism translates and generates database schemas automatically (`db.create_all()`). This encapsulates our database architecture directly into programmatic logical models, facilitating simpler, secure integration alongside version control directly inside `app.py`, without requiring the developer to execute any disjoint DB setup or SQL syntax before operating the application.

## 2.1.3.3. Structure of the application
### 2.1.3.3.2. Standard MVC server side page rendering
We adopted a **Standard MVC (Model-View-Controller) server-side page rendering** strategy natively, classifying it structurally as a Multi-Page Application (MPA). 
* **Model:** Handles relational object mapping connecting to the underlying SQLite database seamlessly using SQLAlchemy definitions within `app.py`.
* **View:** Built out safely rendering frontend user representations mainly utilizing flexible HTML paired structurally with Jinja2 template bindings (`templates/*.html`).
* **Controller:** Expressed explicitly through standard scalable Flask view router endpoints (`@app.route(...)`) dictating and mapping programmatic logic to template payloads and managing dynamic client requests reliably.

## 2.1.3.4. Frontend Structure
### 2.1.3.4.1. What kind of frontend has been used and why?
A standard robust **web page frontend** using base interactive web languages alongside a modernized CSS interface grid layout framework (`Bootstrap`).
**Why?**
- **Simplicity & Speed:** Minimizes external dependency weight drastically compared to single-page applications frameworks structurally (e.g., React/Angular/Vue), while producing dynamic, rapid structurally sound web formatting responsively leveraging predefined Bootstrap utilities deeply.
- **Immediate Server-Rendered Availability:** Jinja2 integrates logic natively into structural markup resolving rapidly via direct HTTP routing configurations—handling server-side dynamic template matching explicitly, aligning beautifully considering assignment simplicity directives successfully.

### 2.1.3.4.2. Frontend Choice
- Compatible Output: Readily accessible server-rendered **web page frontends** natively capable of responsive scaling.

## 2.1.3.5. Build and install

### 2.1.3.5.1. Environment details along with list of dependencies
**Environment Details:** Local generic Python 3.x execution environment instances.

**List of Dependencies:**
- `Flask`: High-velocity routing framework logic handler.
- `Flask-SQLAlchemy`: Lightweight interface component dynamically attaching ORM database modeling functionality directly interacting inside the runtime context effortlessly.

### 2.1.3.5.2. Instructions on how to compile or build a project
Given Python functions reliably as a purely interpreted procedural scripting language parsing natively over execution, additionally dynamically creating SQLite schemas safely during start procedures (`db.create_all()`), external discrete traditional build and separate compilation deployment pipeline actions are entirely unnecessary before usage mapping.

### 2.1.3.5.3. Instructions on how to run or install the project
1. Verify a stable functional Python 3 environment is currently operational locally through testing (`python --version`) inside your terminal instance console.
2. Formally connect environment packages interacting efficiently utilizing PIP installations directly:
   ```bash
   pip install flask flask-sqlalchemy
   ```
3. Boot the local procedural web server process dynamically—triggering also initial baseline dynamic `.db` local schema file injection setup dynamically across execution runtime contexts interactively natively from execution entry point commands manually natively executed explicitly:
   ```bash
   python app.py
   ```
4. Experience directly the functional interface structure dynamically connecting across browser tab targeting explicitly: `http://localhost:5000/`.
