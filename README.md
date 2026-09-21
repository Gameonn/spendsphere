# Spendly — Personal Expense Tracker

Spendly is a lightweight Flask web app for logging expenses, understanding
spending patterns, and keeping track of where your money goes. It's built as
a guided, step-by-step learning project — the routing, templates, and styling
are in place, and core functionality (database, auth, and expense CRUD) is
implemented incrementally as numbered steps.

## Features

- **Landing page** — product overview with a call to action to register or sign in
- **Register / Login pages** — account creation and authentication (UI scaffolded)
- **Expense logging** — add, edit, and delete expenses (category, amount, date, description)
- **Spending insights** — category breakdowns and monthly summaries (planned)
- **Date filtering** — view spending over a custom time range (planned)

## Tech Stack

| Layer     | Technology              |
|-----------|--------------------------|
| Backend   | Python 3, [Flask](https://flask.palletsprojects.com/) 3.1 |
| Database  | SQLite                   |
| Frontend  | Jinja2 templates, vanilla CSS/JS |
| Testing   | pytest, pytest-flask     |

## Project Structure

```
expense-tracker/
├── app.py                  # Flask app and route definitions
├── database/
│   ├── __init__.py
│   └── db.py                # get_db() / init_db() / seed_db()
├── templates/
│   ├── base.html             # Shared layout (nav, footer)
│   ├── landing.html          # Marketing landing page
│   ├── login.html            # Login form
│   └── register.html         # Registration form
├── static/
│   ├── css/style.css         # App styling
│   └── js/main.js            # Client-side scripts
├── requirements.txt         # Python dependencies
└── install.cmd               # Claude Code installer (Windows, unrelated to the app)
```

## Getting Started

### Prerequisites

- Python 3.10+ installed and available as `python`/`python3`

### Setup

1. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv

   # macOS/Linux
   source venv/bin/activate

   # Windows (Git Bash)
   source venv/Scripts/activate

   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python app.py
   ```

   The app starts in debug mode at **http://127.0.0.1:5001**.

### Running Tests

```bash
pytest
```

## Routes

| Route                        | Method | Status                        |
|-------------------------------|--------|--------------------------------|
| `/`                            | GET    | Landing page                   |
| `/register`                    | GET    | Registration page              |
| `/login`                       | GET    | Login page                     |
| `/logout`                      | GET    | Placeholder — Step 3           |
| `/profile`                     | GET    | Placeholder — Step 4           |
| `/expenses/add`                | GET    | Placeholder — Step 7           |
| `/expenses/<id>/edit`          | GET    | Placeholder — Step 8           |
| `/expenses/<id>/delete`        | GET    | Placeholder — Step 9           |

## Roadmap

This project is built incrementally. Upcoming steps include:

1. Database setup (`database/db.py`: `get_db()`, `init_db()`, `seed_db()`)
2. User registration & login (authentication)
3. Logout functionality
4. User profile page
5. Expense model & listing
6. Expense form validation
7. Add expense
8. Edit expense
9. Delete expense
10. Spending summaries & category breakdowns

## License

No license specified.
