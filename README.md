# DevCloud Web Application

This is a Django-based web application designed as part of the DevCloud challenge. The app enables users to manage a list of people, perform CRUD operations, authenticate via Google, and calculate financial summaries.


---
## Features

### User Authentication:
Login via Google OAuth for enhanced security.

### CRUD Operations:

- Create: Add a new person with their details (Name, Date of Birth, Dollar Amount).
- Read: View a list of registered people in a table format.
- Update: Edit and update details for an existing person.
- Delete: Remove a person from the database.
- Search: Filter the table by a person's name.

### Currency Conversion:
- Convert a person's dollar amount to reais based on a user-provided exchange rate.

### Financial Calculations:
- Calculate the total and average dollar amounts across all registered people.

## Technologies Used
- Framework: Django
- Frontend: HTML, CSS (optionally styled with Bootstrap)
- Database: SQLite (default Django database)


---
## Installation and Setup

### 1. Clone the repository:

```bash
git clone kenzokomati/desafio-realcloud  
cd desafio-realcloud 
```

### 2. Create a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On MacOS:
source venv/bin/activate 
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```
  
### 4. Apply database migrations:

```bash
python manage.py migrate
```

### 5. Run the development server:

```bash
python manage.py runserver  
```

### 6. Configure Google Login:

1. Set up a Google OAuth project at [Google Cloud Console](https://console.cloud.google.com/).
2. In the Django admin interface, go to the **"Social Applications"** section. If you haven't yet, you'll need to install and configure `django-allauth` or similar packages to enable social authentication.
3. Create a new social application and select **Google** as the provider.
4. Fill in the **Client ID** and **Client Secret** obtained from the Google OAuth project you set up.
5. Save the application settings, and the Google login should be fully integrated.



---
## How to Use

### Login: 
Use the Google login feature to access the application. 

### Manage People:
Use the "Create" button to add a person.

Edit or delete existing entries using the buttons next to each entry in the table.

Filter by name using the search bar.

### Currency Conversion: 
Enter a person's ID and the exchange rate to convert their dollar amount to reais.

### Financial Summary: 
Click the button to calculate and display the total and average dollar amounts for all registered people.


---
## Known Limitations
- Graph Visualization: The bar chart visualization feature is currently not implemented.
- Deployment: The application is not yet hosted on a cloud platform.
