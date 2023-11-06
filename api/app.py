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
            "https://api.github.com/users/" + input_git_username + "/repos"
            )
    if response.status_code == 200:
        repos = response.json()
        repo_list = []
        for repo in repos:
            repo_list.append(repo["full_name"])
    return render_template(
            "hello.html", name=input_name,
            age=input_age, colour=input_fav_colour,
            username=input_git_username,repo=repo_list
            )
