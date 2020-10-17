from flask import Flask, render_template
import gunicorn
import subprocess

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    p = subprocess.Popen(['python -m SimpleHTTPServer'], shell=True)
    app.run(host='localhost', port=8000)
