import os
import win32com.client as win32
from flask import Flask, render_template, request, redirect, url_for
from gevent.pywsgi import WSGIServer

from utils.corespondence import DataCorrespondence
from utils.function import read_cell
from utils.model import Address, SimulationResult
import pythoncom

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/simulate', methods=["POST", "GET"])
def result():
    pythoncom.CoInitialize()
    engine_file = os.path.join(os.getcwd(), "simulateur.xlsx")

    data = SimulationResult()
    data.profit_before_all = read_cell(engine_file, DataCorrespondence.profit_before_all_contribution)
    data.IR.before_contribution = read_cell(engine_file, DataCorrespondence.profit_before_contribution_ir)
    data.IS.before_contribution = read_cell(engine_file, DataCorrespondence.profit_before_contribution_is)
    data.IR.contribution = read_cell(engine_file, DataCorrespondence.contribution_ir)
    data.IS.contribution = read_cell(engine_file, DataCorrespondence.contribution_is)
    
    return render_template("result.html", result=data)


if __name__ == '__main__':
    # Debug/Development
    app.run(debug=True, host="0.0.0.0", port="5001")
    # Production
    # http_server = WSGIServer(('', 5001), app)
    # http_server.serve_forever()

