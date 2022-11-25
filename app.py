from flask import Flask, jsonify, request, abort, Response
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getreq():
    args = request.args.get("category")
    f = open('data.json')
    data = json.load(f)
    if (args != None and args != ""):
        try:
            return jsonify({"data": {args: data["data"][0][args]}})
        except:

            return jsonify({"data": "incorrect Category Name"})
    else:
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
