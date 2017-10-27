from impl.simulator import simulator
from flask import Flask, render_template, request, url_for, redirect, current_app

app = Flask(__name__)

# not so good again...
sim = simulator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/doc')
def doc():
    return render_template('doc.html')


@app.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        sim.create(request.form)
        return redirect(url_for('simulate'))
    return render_template('config.html')


@app.route('/simulate/')
@app.route('/simulate/<statistics>')
def simulate(statistics=None):
    sim.start()
    counter = 0
    while True and counter <= sim.limit:
        sim.event(sim.next_time())
        if not sim.lef:
            break
        counter += 1
    sim.finish()
    stats = sim.statistics
    sim.restart()
    return render_template('simulate.html', statistics=stats)


def debug():
    assert not current_app.debug

# for tests
if __name__ == '__main__':
    simul = simulator()

    test_form = {'limit_queue': 0,
                 'nro_eventos': 100,
                 'tec1_aleatory': '0',
                 'tec_c1': 10,
                 'tec2_aleatory': '4',
                 'tec_e2': 4,
                 'ts1_aleatory': '0',
                 'ts_c1': 10,
                 'ts2_aleatory': '4',
                 'ts_e2': 15,
                 'tef_aleatory': '4',
                 'tef_e': 18,
                 'tf_aleatory': '4',
                 'tf_e': 34}
    simul.create(test_form)
    simul.start()
    counter = 0
    while True and counter <= simul.limit:
        simul.event(simul.next_time())
        if not simul.lef:
            break
        counter += 1
    simul.finish()
