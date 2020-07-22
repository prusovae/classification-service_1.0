from flask import Flask
from flask import request
from profilling.master_route_function import master_route_func

app = Flask(__name__)

@app.route("/", methods=["POST"])
def profileController(text="", prediction_message=""):
    content = request.json
    if content["data"]:
        domain = master_route_func(content)
        return domain
    else:
        return {'dmn': 'DMN_NO_PND', 'percent': 0.0}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
