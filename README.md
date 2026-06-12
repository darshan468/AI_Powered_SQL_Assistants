### AI Powered SQL Assistant 🚀
An AI-powered SQL Assistant that allows users to query databases using natural language. The system automatically converts user questions into SQL queries, executes them on a SQLite database, and displays structured results through an interactive web interface.

# Overview
Business users often struggle with writing SQL queries. This project bridges that gap by enabling users to ask questions in plain English while the AI generates and executes the corresponding SQL query.

# Example

**User Question**

Which product has the highest price?

**Generated SQL**

SELECT * 
FROM products
ORDER BY price DESC
LIMIT 1;

# Result

Laptop Pro
Price: 1499

# Features

* Natural Language to SQL Conversion
* AI-powered Query Generation
* SQLite Database Integration
* Read-only Query Execution
* SQL Safety Validation
* Interactive Chat Interface
* Schema-aware Query Generation
* Real-time Query Results
* Modern Responsive UI
* FastAPI Backend API

## Technology Stack

**Backend**

Python
FastAPI
SQLite
SQLAlchemy

**AI Integration**

Google Gemini API

**Frontend**

HTML5
CSS3
JavaScript

**Database**

SQLite

## Project Structure

AI Powered SQL Assistants/
│
├── backend/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   └── sql_engine.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── scratch/
│
├── .env
├── .env.example
├── .gitignore
├── init_db.py
├── list_models_to_file.py
├── list_models.py
├── models.txt
├── requirements.txt
├── sql_assistant.db
├── test_key.py
└── README.md

# Database Schema

**Customers**

| Column  | Type    |
| ------- | ------- |
| id      | INTEGER |
| name    | TEXT    |
| email   | TEXT    |
| country | TEXT    |

**Products**

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| name     | TEXT    |
| category | TEXT    |
| price    | REAL    |
| stock    | INTEGER |

**Orders**

| Column      | Type    |
| ----------- | ------- |
| id          | INTEGER |
| customer_id | INTEGER |
| date        | DATE    |
| total       | REAL    |

**OrderItems**

| Column     | Type    |
| ---------- | ------- |
| id         | INTEGER |
| order_id   | INTEGER |
| product_id | INTEGER |
| quantity   | INTEGER |

# User Interface

**Main Dashboard**
The application provides:

* Database schema viewer
* AI chat interface
* SQL query display
* Query execution results
* Interactive response system

# Author
**Darshan S**

# GitHub:
https://github.com/darshan468

# License
This project was developed for educational purposes, AI engineering practice, and technical interview demonstrations.

# Application Screenshots

<img width="1891" height="905" alt="Screenshot 2026-06-12 162226" src="https://github.com/user-attachments/assets/0c5f5233-a3d0-4d19-90a7-d3a01c271b05" />
<img width="1896" height="910" alt="Screenshot 2026-06-12 162356" src="https://github.com/user-attachments/assets/49ffa630-ca43-4ad2-8694-7a2c6b051044" />
<img width="1916" height="967" alt="Screenshot 2026-06-12 164044" src="https://github.com/user-attachments/assets/bc2c73de-93cf-4798-a999-e3c6412e8c07" />




