import http
from http.client import BAD_REQUEST

from flask import Flask, request, jsonify

from app.loan.exceptions.param_missed import ParamMissedException
from app.ports.load_from_request import LoanFromArgRequest
from app.services.loan_service import LoanService

app = Flask(__name__)

port = LoanFromArgRequest()
service = LoanService()

@app.route("/")
def hello_world():
    return "Loan project is running!"


@app.route("/apr")
def apr():
    try:
        desire = port.execute(request.args)
        percent = service.execute(desire)
    except ParamMissedException as pe:
        return jsonify(f"Invalid execution. Param {pe.get_param()} is missed"), http.client.BAD_REQUEST
    return jsonify(percent), http.client.OK


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)


