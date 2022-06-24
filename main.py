from db import database
from flask import Flask, request, jsonify

database = database

app = Flask(__name__)


@app.route("/")
def hello():
    return "a"


@app.route("/as-number")
def returnAsNumber():
    try:
        data = request.get_json()
        res = database.selectAsNumber(database(), data.get("number"))
        print(res)
        if res:
            return jsonify(res)
        else:
            return "The AS number doesn't exist"
    except Exception as e:
        return e

@app.route("/ip")
def returnIPinfo():
    try:
        data = request.get_json()
        res = database.selectIPadd(database(), data.get("ip"))
        if res:
            return jsonify(res)
        else:
            return "The IP doesn't exist"
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run(debug=True)
