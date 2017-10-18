from impl.simulator import simulator
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# not so good again...
sim = simulator()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/doc")
def doc():
    return "Documentação em breve!"


@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        sim.create(request.form)
        return redirect(url_for('simulate'))
    return render_template('config.html')


@app.route("/simulate")
def simulate():
    # usar ideias de steps para view de execução com possibilidade de
    # finalizar.
    # 2 radio button com 1 submit, valor define como agir
    sim.start()
    while not sim.lef:
        sim.next_time()
        sim.event()
    sim.finish()
    return render_template('simulate.html')
