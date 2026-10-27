# Advanced Expense Tracker

A web-based expense tracking application built using Python, Django, and PostgreSQL. It allows users to manage expense records, view spending summaries, and analyze expense patterns through a dashboard with charts and tables.

## Features

- **Expense Management:** Add, edit, and delete expense records.
- **Expense Categories:** Organize expenses into 17 predefined categories.
- **Input Validation:** Validate expense names, amounts, and dates.
- **Expense Dashboard:** View spending summaries for the last 7, 30, and 365 days.
- **Category-wise Analysis:** View expense distribution through a doughnut chart and summary table.
- **Daily Expense Trends:** Visualize daily spending using a line chart.
- **Expense History:** View recorded expenses ordered by date.
- **Dark-themed Interface:** Display expense information in a dashboard layout.

## Technologies Used

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Tailwind CSS
- **Charts:** Chart.js
- **Environment Configuration:** python-dotenv
- **Database Adapter:** psycopg2-binary
- **Version Control:** Git and GitHub

## Project Structure

```text
advanced-expense-tracker/
├── config/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── expenses/
│   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   ├── templates/
│   │   │   └── expenses/
│   │   │       ├── base.html
│   │   │       ├── dark-modern-index.html
│   │   │       ├── edit.html
│   │   │       ├── index.html
│   │   │       └── modern-edit.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── validators.py
│   │   └── views.py
│   └── manage.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12 or a compatible version
- PostgreSQL
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Priyanka-tech19/advanced-expense-tracker.git
cd advanced-expense-tracker
```

### 2. Create and Activate a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the repository root, alongside `README.md` and `requirements.txt`.

Add your local configuration:

```dotenv
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

Replace the placeholder values with your own configuration. Do not commit your `.env` file or expose real credentials.

### 5. Set Up PostgreSQL

Create the PostgreSQL database specified by `DB_NAME` and ensure the configured database user has the required permissions.

### 6. Run Database Migrations

From the repository root:

```powershell
cd config
python manage.py migrate
```

### 7. Start the Development Server

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Backend Implementation

- Validates expense names, amounts, and dates.
- Uses Django ORM with PostgreSQL to calculate expense summaries and category-wise totals.
- Displays daily spending trends and category distribution using Chart.js.

## Configuration and Security

- Loads sensitive configuration values from environment variables.
- Excludes `.env` files and virtual environments from version control.
- Currently intended for local development, not production hosting.

## Author

**Priyanka**

GitHub: https://github.com/Priyanka-tech19
