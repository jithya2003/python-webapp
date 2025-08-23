from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-size: 48px;
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    margin: 0;
                }
            </style>
        </head>
        <body>
            DevSecOps with Trivy + SonarQube!
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)