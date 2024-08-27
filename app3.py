"""
This module sets up a Flask application that serves user data from a JSON file.

It includes:
- Reading user data from 'users.json'.
- Appending new user data to 'users.json'.
- Providing an endpoint to return the user data in JSON format.
"""

import json
import flask

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "Kostya"


@app.route("/test")
def test():
    """
    Endpoint to retrieve and display the list of users from 'users.json'.

    Returns:
        flask.Response: JSON response containing the list of users.
    """
    with open("users.json", "r", encoding="utf-8") as read_file:
        users_data = json.load(read_file)
        for user in users_data:
            print(user)
        return flask.jsonify(users_data)


if __name__ == "__main__":
    # Append new user data to 'users.json'
    with open("users.json", "r+", encoding="utf-8") as write_file:
        existing_data = json.load(write_file)
        existing_data.append({"name": "Ira", "email": "ira@gmail.com"})
        write_file.seek(0)  # Move file pointer to the beginning
        json.dump(existing_data, write_file, indent=4)
        write_file.truncate()  # Remove any remaining part of the old file

    app.run(debug=True, port=8000)
