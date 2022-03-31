from flask import Flask, request, Response

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
    desire = port.execute(request.args)
    percent = service.execute(desire)
    return Response(response=str(percent), status=201)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)


