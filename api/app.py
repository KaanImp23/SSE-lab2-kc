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
        repo_name = []
        sentence_list = []
        for repo in repos:
            repo_list.append(repo["full_name"])
            repo_name.append(repo["full_name"])
            repo_list.append(repo["updated_at"])
        dict_repo = {}
        for i in range(0, len(repo_list), 2):
            dict_repo[repo_list[i]] = repo_list[i + 1]
        for k, v in dict_repo.items():
            sentence = "Repository: " + str(k) + \
                " was last updated at " + v
            sentence_list.append(sentence)
            sentence1 = sentence_list[0]
            sentence2 = sentence_list[1]
            sentence3 = sentence_list[2]
            sentence4 = sentence_list[3]
            sentence5 = sentence_list[4]
    return render_template(
            "hello.html", name=input_name,
            age=input_age, colour=input_fav_colour,
            username=input_git_username, dictrepo=dict_repo,
            sentence1=sentence1, sentence2=sentence2,
            sentence3=sentence3, sentence4=sentence4,
            sentence5=sentence5
            )


@app.route('/submit/details', methods=["POST"])
def details():
    repo_name = request.form.get("reponame")
    commit_response = requests.get(
            "https://api.github.com/repos/" + repo_name +
            "/commits"
            )
    if commit_response.status_code == 200:
        com_sha = []
        com_author = []
        com_date = []
        com_message = []
        com = commit_response.json()
        for commit in com:
            com_sha.append(commit["commit"]["tree"]["sha"])
            com_author.append(commit["commit"]["author"]["name"])
            com_date.append(commit["commit"]["committer"]["date"])
            com_message.append(commit["commit"]["message"])
        com_sha1 = com_sha[0]
        com_sha2 = com_sha[1]
        com_sha3 = com_sha[2]
        com_sha4 = com_sha[3]
        com_sha5 = com_sha[4]
        com_author1 = com_author[0]
        com_author2 = com_author[1]
        com_author3 = com_author[2]
        com_author4 = com_author[3]
        com_author5 = com_author[4]
        com_date1 = com_date[0]
        com_date2 = com_date[1]
        com_date3 = com_date[2]
        com_date4 = com_date[3]
        com_date5 = com_date[4]
        com_message1 = com_message[0]
        com_message2 = com_message[1]
        com_message3 = com_message[2]
        com_message4 = com_message[3]
        com_message5 = com_message[4]
        return render_template(
            "commit_details.html", reponame=repo_name,
            sha1=com_sha1, author1=com_author1,
            date1=com_date1, message1=com_message1,
            sha2=com_sha2, author2=com_author2,
            date2=com_date2, message2=com_message2,
            sha3=com_sha3, author3=com_author3,
            date3=com_date3, message3=com_message3,
            sha4=com_sha4, author4=com_author4,
            date4=com_date4, message4=com_message4,
            sha5=com_sha5, author5=com_author5,
            date5=com_date5, message5=com_message5)


@app.route('/query')
def query():
    query_parameter = request.args.get('q')
    return process_query(query_parameter)


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"
