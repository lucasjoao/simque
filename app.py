from impl.simulator import simulator
from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
# not so good...
app.secret_key = 'V\xf5\xa1\xa3\xb0\xaf\x179\x82+J6'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/doc")
def doc():
    return "Documentação em breve!"


@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        session['simulator'] = request.form
        return redirect(url_for('simulate'))
    return render_template('config.html')


@app.route("/simulate")
def simulate():
    sim = simulator(session['simulator'])
    sim.start()
    while not sim.lef:
        sim.next_time()
        sim.event()
    sim.finish()
    return render_template('simulate.html')
