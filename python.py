from flask import Flask, render_template
import requests
import json


app = Flask(__name__, template_folder=".")


@app.route("/")
def homepage():
    with open('/tmp/menus.json', 'r') as f:
    	return render_template("python.html", menus=json.loads(f.read())["Date"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
