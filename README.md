# 💰 Expense Tracker Web Application 

A Django-powered web application that helps users track their expenses category-wise, set monthly budgets, and visualize spending trends using charts.

## Features

-  Add and categorize expenses
-  View expenses for:
  - Past 1 week
  - Past 1 month
  - Past 1 year
-  Set and manage a monthly budget
- Visual reports using:
  - **Pie charts** for category-wise expense distribution
  - **Bar charts** for comparative analysis
-  Get insights on whether you're within budget or overspending

## 🛠 Tech Stack

- **Frontend:** HTML, CSS  
- **Backend:** Django, Python  
- **Data Visualization:** Matplotlib  

## Project Structure
mysite/
│
├── myapp/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │   └── myapp/
│   │       ├── images/
│   │       ├── src.css
│   │       ├── style.css
│   │       └── styles.css
│   ├── templates/
│   │   └── myapp/
│   │       ├── base.html
│   │       ├── edit.html
│   │       ├── index.html
│   │       └── templatetags/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── mysite/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

## Follow these steps to set up and run the Expense Tracker project locally on your system:

1. 📥 Clone the Repository

git clone https://github.com/28naitik/Expense-Tracker-Project.git
cd Expense-Tracker-Project/mysite

3. Create and Activate a Virtual Environment (Recommended)

For Windows:
python -m venv venv
venv\Scripts\activate

For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

4. Install Required Dependencies

If you have a requirements.txt file:
pip install -r requirements.txt
Or manually install the required packages:
pip install django matplotlib

4.Run Migrations:

python manage.py makemigrations

python manage.py migrate

5.Create a Superuser (Optional for Admin Access):

python manage.py createsuperuser
Follow the prompts to set username, email, and password.

6. Start the Development Server

python manage.py runserver
