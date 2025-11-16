# Office Employee Management System

This is a simple yet robust Employee Management System built with Python and the Django web framework. This project allows a user to perform basic CRUD (Create, Read, Update, Delete) operations on employee records. It's an excellent project for learning the fundamentals of Django and web development.

## 🌟 Features

*   **View All Employees**: A comprehensive list of all employees in the system, showing their details like name, department, role, and hire date.
*   **Add a New Employee**: An easy-to-use form to add new employees to the database.
*   **Remove an Employee**: Functionality to delete employee records from the system.
*   **Filter Employees**: A powerful filtering tool to search for employees by their first/last name, department, or role.
*   **Dynamic Data**: Department and Role choices are dynamically populated from the database.

## 🛠️ Tech Stack

*   **Backend**: Python, Django
*   **Database**: SQLite 3 (default)
*   **Frontend**: HTML, Bootstrap (for basic styling and responsive design)

## 📂 Project Structure

The project follows a standard Django application structure.

```
office_emp_proj/
├── db.sqlite3
├── emp_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── add_emp.html
│   │   ├── all_emp.html
│   │   ├── filter_emp.html
│   │   ├── index.html
│   │   └── remove_emp.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py       # Defines Employee, Role, and Department models
│   ├── urls.py         # URL routing for the employee app
│   └── views.py        # Core application logic
├── manage.py
└── office_emp_proj/
    ├── settings.py     # Project settings
    └── urls.py         # Project-level URL routing
```

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/office_emp_proj.git
    cd office_emp_proj
    ```

2.  **Create and activate a virtual environment (Recommended):**
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required packages:**
    *First, it's a good practice to create a `requirements.txt` file if you don't have one:*
    ```sh
    pip freeze > requirements.txt
    ```
    *Then, install the dependencies:*
    ```sh
    pip install -r requirements.txt
    ```
    *(If you are setting this up for the first time, you will need to install Django first: `pip install django`)*

4.  **Apply database migrations:**
    This will create the necessary tables in your `db.sqlite3` file based on the models defined in `emp_app/models.py`.
    ```sh
    python manage.py migrate
    ```

5.  **Create a superuser (Optional):**
    This allows you to access the Django admin panel to manage data directly.
    ```sh
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at http://127.0.0.1:8000/.

## 📖 How to Use

1.  Navigate to the home page to see the main menu.
2.  Click on **"View All Employees"** to see a table of all current employees.
3.  Click on **"Add An Employee"** to go to a form where you can input new employee details.
4.  Click on **"Remove An Employee"** to see a list of employees with an option to delete each one.
5.  Click on **"Filter Employee Details"** to search for specific employees based on their name, department, or role.

---
*This project was created as a learning exercise to understand the core concepts of the Django framework.*
