from flask import Flask, render_template, url_for


myPorts = {
    24: {'name': 'Теплица Свет', 'portDir': 'out', 'state': 'low'},
    25: {'name': 'Teplica Cvet', 'portDir': 'out', 'state': 'high'},
    23: {'name': 'Teplica', 'portDir': 'out', 'state': 'high'},
    27: {'name': 'Water Level', 'portDir': 'in', 'state': 'low'}
    }


app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    print(url_for('index'))
    return render_template('index.html')

@app.route('/control/')
def controlpanel():
    return render_template('controlpanel.html',
                           ports = myPorts)

@app.route('/dop/')
def index1():
    return render_template('base.html', title = 'addition', menu = '23')


if __name__ == '__main__':
    app.run(debug=True, port=5003, host='0.0.0.0')

    
