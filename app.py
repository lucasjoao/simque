from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/doc")
def doc():
    return "Documentação em breve!"

@app.route("/config")
def config():
    return "Configuração em breve!"
