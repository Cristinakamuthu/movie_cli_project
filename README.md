# movie_cli_project
# 🎬 Movies CLI App

This is a simple command-line app that helps manage a list of movies, their main actors, and directors.

## 📌 What It Does

- You can add new movies  
- You can view all movies  
- You can update movie details  
- You can delete a movie  
- Each movie is linked to a main actor and a director

## 🧠 Models Used

- **Movie** – has a title and release year, belongs to one actor and one director  
- **Actor** – has a name and age, can act in many movies  
- **Director** – has a name and style, can direct many movies  

## 🛠 How to Run It

1. Clone this repo:
   ```bash
   git clone <your-repo-link>
   cd movie_cli_project

Install dependencies:

bash
Copy
Edit
pipenv install
Activate the environment:

bash
Copy
Edit
pipenv shell
Set up the database:

bash
Copy
Edit
python lib/models/__init__.py
python lib/seed.py
Start the CLI:

bash
Copy
Edit
python lib/cli.py
📂 Folder Structure
pgsql
Copy
Edit
movie_cli_project/
│
├── lib/
│   ├── cli.py
│   ├── debug.py
│   ├── helper.py
│   ├── seed.py
│   └── models/
│       ├── __init__.py
│       ├── actor.py
│       ├── director.py
│       └── movie.py
│
├── Pipfile
├── Pipfile.lock
└── README.md

