# BayRecruit Multi-Cloud AI Operations Dashboard

## Project Overview

BayRecruit Multi-Cloud AI Operations Dashboard is an end-to-end cloud engineering and DevOps project that demonstrates a centralized monitoring platform for AWS, Azure, and GCP environments.

The platform includes a company dashboard, system health monitoring, AI operations tools, and a Flask backend API. It allows users to check cloud health, alerts, deployment status, logs, incidents, cost analysis, optimization suggestions, and troubleshooting guidance from one dashboard.

## Tech Stack

Frontend:
HTML, CSS, JavaScript, Nginx

Backend:
Python, Flask, Flask-CORS

DevOps:
Docker, Docker Desktop, Git, GitHub

Cloud Concepts:
AWS, Azure, GCP, ECS/Fargate, CloudWatch, SNS, Azure Entra ID, Multi-cloud monitoring

Database:
AWS DynamoDB

## Features

Centralized multi-cloud dashboard  
System health monitor for AWS ECS, Azure VM, GCP Storage, and Database  
AI Operations Center with multiple smart tools  
Flask backend API for AI responses  
Dockerized frontend and backend  
Frontend-to-backend API integration  
GitHub version control and commit history  
Simulated multi-cloud monitoring use case  
Professional portfolio-ready cloud project  

## AI Operations Tools

Ask Cloud AI  
Analyze Alerts  
Review Deployment  
Summarize Logs  
Detect Incident  
Get Optimization  
Analyze Cost  
Troubleshoot  

## How to Run with Docker

### Run Backend

Open terminal inside the backend folder:

```bash
cd backend
docker build -t todo-backend .
docker run -d -p 5000:5000 --name todo-backend todo-backend
```

Test backend:

```text
http://localhost:5000
```

Expected output:

```text
Backend is running successfully
```


### Run Frontend

Open terminal inside the frontend folder:

```bash
cd frontend
docker build -t todo-frontend .
docker run -d -p 8080:80 --name todo-frontend todo-frontend
```

Open dashboard:

```text
http://localhost:8080/dashboard.html
```
