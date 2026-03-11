# django-hit237-week2-practicals-v4
Hit237 Week 2 Practical Sessions

## Setup (Windows)

1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

2. Upgrade pip and install dependencies:

```powershell
python -m pip install --upgrade pip
pip install django
```

3. Create the Django project (already created in repo):

```powershell
django-admin startproject project_blog .
```

4. Initialize the database and run the development server:

```powershell
python manage.py migrate
python manage.py runserver
```

5. Save dependencies:

```powershell
pip freeze > requirements.txt
```

Notes:
- The virtual environment folder `.venv/` is ignored by `.gitignore`.
- If PowerShell blocks activation, open CMD and run `.venv\Scripts\activate.bat` instead.
