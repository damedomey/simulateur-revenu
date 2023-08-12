import os
import shutil
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from gevent.pywsgi import WSGIServer

from utils.corespondence import DataCorrespondence
from utils.function import read_cell, write_cell
from utils.model import Address, SimulationResult

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/questionnaire')
def questionnaire():
    return render_template("questionnaire.html")

@app.route('/simulate', methods=["POST", "GET"])
def result():
    return render_template("result.html", result=SimulationResult())


if __name__ == '__main__':
    # # Debug/Development
    app.run(debug=True, host="0.0.0.0", port="5001")
    # Production
    #http_server = WSGIServer(('0.0.0.0', 80), app)
    #http_server.serve_forever()

