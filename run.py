import os
import shutil
from datetime import datetime

from win32com import client as winClient
from flask import Flask, render_template, request, redirect, url_for
from gevent.pywsgi import WSGIServer

from utils.corespondence import DataCorrespondence
from utils.function import read_cell
from utils.model import Address, SimulationResult
import pythoncom

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/simulate', methods=["POST", "GET"])
def result():
    pythoncom.CoInitialize()

    engine_file = os.path.join(os.getcwd(), "simulateur.xlsx")
    # Duplicate the original file as the temporary file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    temp_file_path = os.path.join(os.getcwd(), "tmp", f"temp_copy_{timestamp}.xlsx")
    shutil.copyfile(engine_file, temp_file_path)

    excel_app = winClient.Dispatch("Excel.Application")
    excel_app.Visible = False
    excel_app.DisplayAlerts = False

    workbook = excel_app.Workbooks.Open(temp_file_path)

    data = SimulationResult()
    data.profit_before_all = read_cell(workbook, DataCorrespondence.profit_before_all_contribution)
    data.IR.before_contribution = read_cell(workbook, DataCorrespondence.profit_before_contribution_ir)
    data.IS.before_contribution = read_cell(workbook, DataCorrespondence.profit_before_contribution_is)
    data.IR.contribution = read_cell(workbook, DataCorrespondence.contribution_ir)
    data.IS.contribution = read_cell(workbook, DataCorrespondence.contribution_is)

    # todo: Save, close the file and release resources
    workbook.Save()
    # workbook.Close()
    # excel_app.Quit()
    # os.remove(temp_file_path)

    return render_template("result.html", result=data)


if __name__ == '__main__':
    # Debug/Development
    app.run(debug=True, host="0.0.0.0", port="5001")
    # Production
    # http_server = WSGIServer(('', 5001), app)
    # http_server.serve_forever()

