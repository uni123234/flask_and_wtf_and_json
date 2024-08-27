"""
This module sets up a basic Flask application with search functionality.

It includes:
- A search form rendered from 'search.html'.
- A search result page that displays the search term.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/search/")
def flask_search():
    """
    Renders the search form page.

    Returns:
        str: Rendered HTML for the search form.
    """
    return render_template("search.html")


@app.route("/dosearch/")
def flask_dosearch():
    """
    Handles search queries and returns a result page with the search term.

    Returns:
        str: Message with the search term.
    """
    search_term = request.args.get("s")
    return f"Пошук по {search_term}"


if __name__ == "__main__":
    app.run(debug=True)
