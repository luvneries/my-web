from flask import Flask, render_template
from redis import Redis
import os

app = Flask(__name__)

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

r = Redis(host=REDIS_HOST, port=REDIS_PORT)
r.set('hits',0)

@app.route("/")
def home():
    r.incr('hits')
    return render_template("home.html", nb_visitors = r.get('hits'))

@app.route("/projects")
def my_profile():
    return render_template("projects.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port="3000")
