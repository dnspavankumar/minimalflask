from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Render!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"Test app starting on port {port}")
    app.run(host='0.0.0.0', port=port)
