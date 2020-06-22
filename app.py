# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import determineStone


# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/results', methods=['GET', 'POST'])
def results():
    name = request.form['name']
    month = request.form['month']
    gem = determineStone(month)
    if request.method == 'GET':
        return "ERROR!"
    else:
        return render_template('results.html', name = name, month=month, gem=gem)