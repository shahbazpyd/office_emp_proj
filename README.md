# Office Employee Management System (SaaS Edition)

This is a robust, production-ready Employee Management System built with Python and the Django web framework. This project has been significantly upgraded from a basic CRUD application into a modern SaaS-style portfolio piece featuring a beautiful UI, Role-Based Access Control, data visualization, and cloud deployment readiness.

## 🌟 Features

*   **Interactive Dashboard**: A modern landing page featuring **Chart.js** data visualizations showing employee distribution across departments and roles, plus total payroll metrics.
*   **Role-Based Access Control (RBAC)**: 
    *   **HR Admins** have full privileges to add/remove employees, departments, and roles.
    *   **Regular Employees** have read-only access to view the directory.
*   **Modern UI & UX**: Completely overhauled with **Bootstrap 5**, custom CSS (glassmorphism effects, sidebar navigation), and interactive toast notifications for feedback.
*   **AJAX Search & Export**: Instantly filter the employee directory without reloading the page, and export the employee list directly to CSV.
*   **Secure Forms & Validation**: Utilizes Django `ModelForms` with custom validation (e.g., ensuring 10-digit phone numbers and non-negative salaries).
*   **Cloud Ready**: Fully configured for deployment on **Vercel** with a **Neon PostgreSQL** database.

## 🛠️ Tech Stack

*   **Backend**: Python, Django
*   **Database**: Neon PostgreSQL (Production), SQLite 3 (Local Fallback)
*   **Frontend**: HTML5, Bootstrap 5, Chart.js, FontAwesome, Custom CSS
*   **Deployment**: Vercel ready (via `vercel.json` and `whitenoise` for static files)

## 📂 Project Structure

```
office_emp_proj/
├── emp_app/
│   ├── templates/          # HTML Templates (Base layout, Dashboard, Forms)
│   ├── forms.py            # Secure ModelForms and Validation
│   ├── models.py           # Employee, Role, and Department Database Models
│   ├── tests.py            # Automated Unit Tests
│   ├── urls.py             # App-level routing
│   └── views.py            # Core application logic & access control
├── office_emp_proj/
│   ├── settings.py         # Settings configured for local & cloud DBs
│   └── urls.py             # Project-level routing
├── static/                 # Custom CSS and assets
├── .env                    # Environment variables (Database URL, Secret Key)
├── package.json            # Vercel build scripts
├── requirements.txt        # Python dependencies
└── vercel.json             # Vercel deployment configuration
```

## 🚀 Getting Started

Follow these instructions to run the project on your local machine.

### Prerequisites
*   Python 3.8+
*   pip

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/office_emp_proj.git
    cd office_emp_proj
    ```

2.  **Create and activate a virtual environment:**
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
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory and add your Neon PostgreSQL Database URL (or leave it out to default to local SQLite):
    ```env
    DATABASE_URL=postgresql://<user>:<password>@<host>/<dbname>?sslmode=require
    SECRET_KEY=your-secret-key
    DEBUG=True
    ```

5.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Run automated tests (Optional but recommended):**
    ```sh
    python manage.py test emp_app
    ```

7.  **Create a superuser:**
    Create an admin account to access the Django admin panel and act as an HR Admin.
    ```sh
    python manage.py createsuperuser
    ```

8.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at http://127.0.0.1:8000/.

## 📖 How to Use

1.  **Dashboard**: Upon logging in, you'll see charts displaying company analytics.
2.  **View & Search**: Click **"All Employees"** to see the directory, or use the **"Filter"** page for advanced searches.
3.  **HR Actions**: If your account belongs to the "HR Admin" group (or is a superuser), you will unlock the sidebar links to **Add Employees**, **Remove Employees**, and manage **Departments/Roles**.
4.  **Export**: Use the CSV export functionality on the employee list page to download records.

---
*This project serves as a showcase of modern Django web development, combining strong backend architecture with a polished user experience.*
