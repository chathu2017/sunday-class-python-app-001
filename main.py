from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # මේකෙන් අපිට බලාගන්න පුළුවන් App එක දුවන Server එකේ විස්තර
    server_info = os.environ.get('COMPUTERNAME', 'Linux Container')
    
    # Minimal සහ Colorful HTML Theme එක
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>App Service Training</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #005A9E, #00BCF2); /* Modern Blue Gradient */
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background-color: #ffffff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
                width: 90%;
            }}
            h1 {{
                color: #005A9E;
                margin-bottom: 20px;
                font-size: 2em;
            }}
            .server-info {{
                background-color: #f3f2f1;
                padding: 15px;
                border-radius: 8px;
                font-size: 1.1em;
                color: #444;
                border-left: 5px solid #00BCF2;
                margin-top: 20px;
            }}
            .icon {{
                font-size: 3.5em;
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">🚀</div>
            <h1>Welcome to App Service Training</h1>
            <p>We are glad to have you here. Let's build something amazing!</p>
            <div class="server-info">
                <strong>⚙️ Running on:</strong><br>
                {server_info}
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)