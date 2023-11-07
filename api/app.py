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
        com_list = []
        for repo in repos:
            repo_list.append(repo["full_name"])
            repo_list.append(repo["updated_at"])
            commits = requests.get(
                "https://api.github.com/repos/" + repo["full_name"] +
                "/commits?per_page=5"
            )
            if commits.status_code == 200:
                coms = commits.json()
                for com in coms:
                    com_list.append(com["commit"]["tree"]["sha"])
                    com_list.append(com["commit"]["author"]["name"])
                    com_list.append(com["commit"]["committer"]["date"])
                    com_list.append(com["commit"]["message"])
    return render_template(
            "hello.html", name=input_name,
            age=input_age, colour=input_fav_colour,
            username=input_git_username, repo=repo_list,
            com=com_list
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
