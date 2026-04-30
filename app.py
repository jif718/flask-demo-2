from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Flask Demo</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }

        .card {
            padding: 50px 80px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
            text-align: center;
            backdrop-filter: blur(10px);
        }

        h1 {
            font-size: 56px;
            margin: 0 0 16px;
        }

        p {
            font-size: 24px;
            margin: 0;
            opacity: 0.9;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello from New Flask Demo v1.5</h1>
        <p>Running on Kubernetes + Helm</p>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
