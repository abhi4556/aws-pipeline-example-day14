# app.py
from flask import Flask
from flask import render_template_string

app = Flask(__name__)

@app.route('/')
def default():
    return render_template_string('<body style="background-color:green;">Welcome to the Home Page!</body>')

@app.route('/blue')
def blue():
    return render_template_string('<body style="background-color:blue;">Welcome to the Blue Page!</body>')

@app.route('/black')
def black():
    return render_template_string('<body style="background-color:black; color:white;">Welcome to the Black Page!</body>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
