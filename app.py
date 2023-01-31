# Import necessary libraries
from flask import Flask, jsonify, request, abort, Response
import json

# Initialize Flask application
app = Flask(__name__)

# Route to handle GET request


@app.route('/', methods=['GET'])
def getreq():
    # Get the value of the "category" argument in the URL query string
    args = request.args.get("category")

    # Open the data.json file
    f = open('data.json')
    data = json.load(f)

    # If the "category" argument is not None or empty
    if (args != None and args != ""):
        try:
            # Return the data for the specified category
            return jsonify({"data": {args: data["data"][0][args]}})
        except:
            # If the specified category is not found, return an error message
            return jsonify({"data": "incorrect Category Name"})
    else:
        # If the "category" argument is None or empty, return all data
        return jsonify(data)


# Main function
if __name__ == "__main__":
    # Start the Flask application in debug mode
    app.run(debug=True)
