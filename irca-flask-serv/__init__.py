import os
import sys
from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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
            print('Test POST or maybe something else', file=sys.stderr)

    @app.route('/test_template')
    @app.route('/test_template/<name>')
    def test_templates(name=None):
        return render_template('test.html', name=name)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app