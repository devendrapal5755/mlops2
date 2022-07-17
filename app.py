

from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import yaml
import joblib

from prediction_service import prediction
webapp_root = "webapp"


static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")
print(static_dir)
print(template_dir)

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pass
        try:
            # if request.form:
            #     data = dict(request.form).values()
            #     data = [list(map(float,data))]
            #     response = predict(data)
            #     return render_template("index.html", response=response)
            # elif request.json:
            #     response = api_response(request)
            #     return jsonify(response)
            if request.form:
                dict_req = dict(request.form)
                response = prediction.form_response(dict_req)
                return render_template("index.html", response=response)

            elif request.json:
                response = prediction.api_response(request.json)
                return jsonify(response)

        except Exception as e:
            print(template_dir)
            print(static_dir)
            print(e)
            # error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}

            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)