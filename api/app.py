from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("git_username.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_fav_colour = request.form.get("colour")
    input_git_username = request.form.get("username")
    response = requests.get(
            "https://api.github.com/users/input_git_username/repos"
            )
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(repo["full_name"])
    return render_template(
            "hello.html", name=input_name,
            age=input_age, colour=input_fav_colour,
            username=input_git_username
            )


@app.route('/query')
def query():
    query_parameter = request.args.get('q')
    return process_query(query_parameter)


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"
