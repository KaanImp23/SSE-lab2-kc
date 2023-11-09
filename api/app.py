from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_fav_colour = request.form.get("colour")
    return render_template(
            "hello.html", name=input_name,
            age=input_age, colour=input_fav_colour
            )


@app.route("/askuser")
def askuser():
    return render_template("git_username.html")


@app.route("/askuser/chooserepo", methods=["POST"])
def chooserepo():
    input_name = request.form.get("name")
    input_fav_colour = request.form.get("colour")
    input_git_username = request.form.get("username")
    random_joke = request.get(
            https://official-joke-api.appspot.com/random_joke
            )
    response = requests.get(
            "https://api.github.com/users/" + input_git_username + "/repos"
            )
    if response.status_code == 200:
        repos = response.json()
        repo_name = []
        repo_update = []
        reponame0 = None
        reponame1 = None
        reponame2 = None
        reponame3 = None
        reponame4 = None
        repoupdate0 = None
        repoupdate1 = None
        repoupdate2 = None
        repoupdate3 = None
        repoupdate4 = None
        for repo in repos:
            repo_name.append(repo["full_name"])
            repo_update.append(repo["updated_at"])
        name_length = len(repo_name)
        update_length = len(repo_update)
        if name_length > 5:
            name_length = 5
        if name_length > 0:
            reponame0 = repo_name[0]
            if name_length - 1 > 0:
                reponame1 = repo_name[1]
                if name_length - 2 > 0:
                    reponame2 = repo_name[2]
                    if name_length - 3 > 0:
                        reponame3 = repo_name[3]
                        if name_length - 4 > 0:
                            reponame4 = repo_name[4]
        if update_length > 5:
            update_length = 5
        if update_length > 0:
            repoupdate0 = repo_update[0]
            if update_length - 1 > 0:
                repoupdate1 = repo_update[1]
                if update_length - 2 > 0:
                    repoupdate2 = repo_update[2]
                    if update_length - 3 > 0:
                        repoupdate3 = repo_update[3]
                        if update_length - 4 > 0:
                            repoupdate4 = repo_update[4]
    return render_template(
            "hello_git_user.html", name=input_name,
            colour=input_fav_colour, username=input_git_username,
            joke=random_joke,
            reponame0=reponame0, reponame1=reponame1, reponame2=reponame2,
            reponame3=reponame3, reponame4=reponame4, repoupdate0=repoupdate0,
            repoupdate1=repoupdate1, repoupdate2=repoupdate2,
            repoupdate3=repoupdate3, repoupdate4=repoupdate4
            )


@app.route('/askuser/chooserepo/details', methods=["POST"])
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
        com_sha0 = None
        com_sha1 = None
        com_sha2 = None
        com_sha3 = None
        com_sha4 = None
        com_author0 = None
        com_author1 = None
        com_author2 = None
        com_author3 = None
        com_author4 = None
        com_date0 = None
        com_date1 = None
        com_date2 = None
        com_date3 = None
        com_date4 = None
        com_message0 = None
        com_message1 = None
        com_message2 = None
        com_message3 = None
        com_message4 = None
        sha_length = len(com_sha)
        author_length = len(com_author)
        date_length = len(com_date)
        message_length = len(com_message)
        if sha_length > 5:
            sha_length = 5
        if author_length > 5:
            author_length = 5
        if date_length > 5:
            date_length = 5
        if message_length > 5:
            message_length = 5
        if sha_length > 0:
            com_sha0 = com_sha[0]
            if sha_length - 1 > 0:
                com_sha1 = com_sha[1]
                if sha_length - 2 > 0:
                    com_sha2 = com_sha[2]
                    if sha_length - 3 > 0:
                        com_sha3 = com_sha[3]
                        if sha_length - 4 > 0:
                            com_sha4 = com_sha[4]
        if author_length > 0:
            com_author0 = com_author[0]
            if author_length - 1 > 0:
                com_author1 = com_author[1]
                if author_length - 2 > 0:
                    com_author2 = com_author[2]
                    if author_length - 3 > 0:
                        com_author3 = com_author[3]
                        if author_length - 4 > 0:
                            com_author4 = com_author[4]
        if date_length > 0:
            com_date0 = com_date[0]
            if date_length - 1 > 0:
                com_date1 = com_date[1]
                if date_length - 2 > 0:
                    com_date2 = com_date[2]
                    if date_length - 3 > 0:
                        com_date3 = com_date[3]
                        if date_length - 4 > 0:
                            com_date4 = com_date[4]
        if message_length > 0:
            com_message0 = com_message[0]
            if message_length - 1 > 0:
                com_message1 = com_message[1]
                if message_length - 2 > 0:
                    com_message2 = com_message[2]
                    if message_length - 3 > 0:
                        com_message3 = com_message[3]
                        if message_length - 4 > 0:
                            com_message4 = com_message[4]
        return render_template(
            "commit_details.html", reponame=repo_name,
            sha1=com_sha0, author1=com_author0,
            date1=com_date0, message1=com_message0,
            sha2=com_sha1, author2=com_author1,
            date2=com_date1, message2=com_message1,
            sha3=com_sha2, author3=com_author2,
            date3=com_date2, message3=com_message2,
            sha4=com_sha3, author4=com_author3,
            date4=com_date3, message4=com_message3,
            sha5=com_sha4, author5=com_author4,
            date5=com_date4, message5=com_message4)


@app.route('/query')
def query():
    query_parameter = request.args.get('q')
    return process_query(query_parameter)


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"
