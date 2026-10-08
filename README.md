# Calculator Website

A simple full-stack calculator website built with Python, FastAPI, HTML, CSS, and JavaScript.

## Live Demo

Try the calculator online:

[Launch Calculator](https://my-calculator-udcb.onrender.com)

## Features
- Add two numbers through a web interface.
- Perform calculations using a Python backend.
- Communicate between frontend and backend via REST API.
- Publicly accessible through cloud deployment.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **Web Server:** Uvicorn
- **Version Control:** Git & GitHub
- **Deployment:** Render

## Project Structure
```text
B4_WebsiteDeveloping_1_Calculator/
├── main.py
├── index.html
├── style.css
├── script.js
├── requirements.txt
└── README.md
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python -m uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/` in your browser.

## Workflow

User Input → JavaScript → FastAPI → Python Calculation → API Response → Website Display

## Purpose

This project was developed to practice the complete web development workflow, from frontend and backend integration to GitHub version control and cloud deployment.
