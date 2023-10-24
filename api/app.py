from flask import Flask, render_template, request
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


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"

@app.route('/query', methods=['GET'])
def query_route():
    q_parameter = request.args.get('q')
    process_query(q_parameter)
