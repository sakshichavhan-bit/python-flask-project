from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Hi I am Sakshi Chavhan, Welcome to my AWS DevOps project!",
        "status": "Application is running",
        "environment": os.getenv("ENVIRONMENT", "dev")
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
