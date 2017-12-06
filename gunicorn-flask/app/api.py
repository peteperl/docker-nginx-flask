import logging
import socket

from flask import Flask, jsonify

log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    return '[Nginx]-[gunicorn-Flask] Dockerized on ECS<br/><br/> Pretend this is our new API:<br/>  /hello<br/>  /echo/aword'

@app.route('/json')
def hello_world():
    return jsonify({
        'hello': 'world'
    })

@app.route('/hello')
def hello():
    return jsonify({
        'hello': 'world',
        'host': socket.gethostname()
    })

@app.route('/echo/<arg>')
def echo(arg):
    return 'ECHO: ' + arg

@app.route('/<path:dummy>')
def fallback(dummy):
    return 'You made it to Flask but that is not a route: ' + dummy

#@app.errorhandler(404)
#def page_not_found(e):
#    return 'You made it to Flask but that is not a route.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
