from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper
import json

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()
# sqlHelper = SQLHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index2.html")

@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    content = request.json["data"]
    print(content)
    song=content["song"]
    preds = modelHelper.recommender(song)
    return(jsonify({"ok": True, "prediction": json.loads(preds.to_json(orient="records"))}))
#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
