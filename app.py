# app.py
import os
from flask import Flask, render_template_string
import boto3

app = Flask(__name__)

SECRET_NAME = "users/app-password"
REGION_NAME = os.getenv("AWS_REGION", "eu-central-1")

def get_secret():
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=REGION_NAME)
    response = client.get_secret_value(SecretId=SECRET_NAME)
    return response['SecretString']

@app.route("/")
def index():
    password = get_secret()
    username = "ElTon Join"
    # Simple HTML template
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Credentials</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .card {{ border: 1px solid #ddd; border-radius: 8px; padding: 20px; width: 300px; }}
            h2 {{ color: #333; }}
            p {{ font-size: 16px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>App Credentials</h2>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Password:</strong> {password}</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
