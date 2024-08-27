import flask
import json

with open("users.json") as file:
    users = json.load(file)
    for user in users:
        print(user)
    users.append({"name": "Ira", "email": "ira@gmail.com"})
    # noinspection PyAssignmentToLoopOrWithParameter
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = "Kostya"


@app.route("/test")
def test():
    with open("users.json") as file:
        users = json.load(file)
        for user in users:
            print(user)
        return flask.jsonify(users)


app.run(debug=True, port=8000)
