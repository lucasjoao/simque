from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/doc")
def doc():
    return "Documentação em breve!"


@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        # TODO: objeto simulador
        # TODO: secret key
        # TODO: realizar um teste de como fazer para pause
        # TODO: algoritmo em si
        session['simulator'] = request.form
        return redirect(url_for('simulate'))
    return render_template('config.html')


@app.route("/simulate")
def simulate():
    print(session['simulator'])
    return render_template('simulate.html')
