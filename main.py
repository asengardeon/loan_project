import http
from http.client import BAD_REQUEST

import dotenv
from flask import Flask, request, jsonify

from app.loan.exceptions.invalid_score_value import InvalidScoreValueException
from app.loan.exceptions.invalid_term import InvalidTermValueException
from app.loan.exceptions.param_missed import ParamMissedException
from app.ports.load_from_request import LoanFromArgRequest
from app.services.loan_service import LoanService

app = Flask(__name__)
port = LoanFromArgRequest()
service = LoanService()


@app.route("/")
def hello_loan():
    return "Loan project is running!"

@app.route("/api/v1/apr")
def apr():
    try:
        desire = port.execute(request.args)
        percent = service.execute(desire)
    except ParamMissedException as pe:
        return jsonify(f"Invalid execution. Param {pe.get_param()} is missed"), http.client.BAD_REQUEST
    except InvalidTermValueException:
        return jsonify(f"Invalid Term value."), http.client.BAD_REQUEST
    except InvalidScoreValueException:
        return jsonify(f"Invalid score value."), http.client.BAD_REQUEST
    return jsonify(percent), http.client.OK


if __name__ == '__main__':
    app.run()


