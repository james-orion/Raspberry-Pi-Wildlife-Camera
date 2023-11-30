from flask import Flask, render_template, request
import json
import subprocess as sp

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    out = sp.run(["php", "images.php"], stdout=sp.PIPE)
    return out.stdout

@app.route("/get_email", methods=["GET"])
def get_email():
    email = request.values["email"]
    print(email)
    return json.dumps(email)

