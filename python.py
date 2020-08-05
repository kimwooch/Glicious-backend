from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__, template_folder=".")

@app.route("/")
def homepage():
    with open('/tmp/menus.json', 'r') as f:
    	return render_template("python.html", menus=json.loads(f.read())["Date"])

#a route to return all of the available menus.
@app.route("/api/v1/menus/all", methods = ["GET"])
def api_all():
    with open('/tmp/menus.json', 'r') as f:
        return jsonify(json.loads(f.read())["Date"])

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(host = '0.0.0.0', port = port)
