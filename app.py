from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/doc")
def doc():
    return "Documentação em breve!"


@app.route("/config", methods=['GET', 'POST'])
def config():
    return render_template('config.html')
