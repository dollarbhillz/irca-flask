from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def this_will_be_index_html():
    return 'This will be index.html'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/test', methods=['GET', 'POST'])
def test_test():
    if request.method == 'GET':
        return 'You just did a GET request.'
    else:
        print 'Test POST or maybe something else'

@app.route('/test_template')
@app.route('/test_template/<name>')
def test_templates(name=None):
    return render_template('test.html', name=name)

