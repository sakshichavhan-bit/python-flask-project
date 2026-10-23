# Python Flask Project

This is a Python Flask application designed to demonstrate a simple web service running in a containerized environment with Docker and automated deployment via Jenkins.

## Project Overview

The project includes:
- A Flask REST API with a home route and health check endpoint
- Docker containerization for deployment
- Jenkins pipeline automation to build, push, and deploy the app
- Environment configuration support

## Tech Stack

- Python 3.12
- Flask 3.1.2
- Docker
- Jenkins
- AWS DevOps workflow oriented setup

## Project Structure

```text
python-flask-project/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
└── .gitignore
```

## Application Details

### Flask App

File: `app/app.py`

The Flask application exposes the following routes:

- `/` : Returns a welcome message, application status, and environment name
- `/health` : Returns the health status with HTTP 200

Example response from `/`:

```json
{
  "message": "Hi I am Sakshi Chavhan, Welcome to my AWS DevOps project!",
  "status": "Application is running",
  "environment": "dev"
}
```

Example response from `/health`:

```json
{
  "status": "healthy"
}
```

### Dependencies

File: `app/requirements.txt`

```txt
Flask==3.1.2
```

### Docker Configuration

File: `Dockerfile`

The Dockerfile does the following:
- Uses Python 3.12 slim base image
- Sets working directory to `/app`
- Installs Python dependencies
- Copies application code into the container
- Sets default environment variable `ENVIRONMENT=dev`
- Exposes port `5000`
- Starts the app with `python app.py`

### Jenkins Pipeline

File: `Jenkinsfile`

The Jenkins pipeline automates:
1. Repository checkout
2. Docker image build
3. Docker image tagging
4. Push to Docker Hub
5. Deployment by running the container on port `8080`

It uses a build tag based on `${BUILD_NUMBER}` and pushes the image to:

```txt
sakshi44/python-flask-app:$IMAGE_TAG
```

## Local Setup

### Prerequisites

- Python 3.12+
- Flask
- Docker
- Git

### Install dependencies

```bash
cd app
pip install -r requirements.txt
```

### Run the application locally

```bash
cd app
python app.py
```

The application will run on:

```txt
http://0.0.0.0:5000
```

## Docker Build and Run

### Build Docker image

```bash
docker build -t python-app:latest .
```

### Run container

```bash
docker run -d -p 8080:5000 python-app:latest
```

Then access:

```txt
http://localhost:8080/
```

## Health Check

```bash
curl http://localhost:8080/health
```

## Environment Variables

- `ENVIRONMENT` : Used to define the runtime environment, defaults to `dev` if not set

## Purpose

This project is a basic example of a Python Flask application used for learning and practicing DevOps automation, including containerization and CI/CD deployment workflows.

## Author

Sakshi Chavhan

## Repository

GitHub: https://github.com/sakshichavhan-bit/python-flask-project
