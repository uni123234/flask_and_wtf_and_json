"""
This module contains a Flask web application for handling luggage registration.

It includes:
- A custom validator to ensure luggage weight does not exceed a specified limit.
- A form class for collecting user details and luggage weight.
- A route to handle GET and POST requests for the luggage form.
"""

import flask
import flask_wtf
import wtforms

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "trade"


def is_luggage_weight_valid(_form, field):
    """
    Custom validator to check if luggage weight is over the limit.

    Args:
        _form (FlaskForm): The form instance (not used in this function).
        field (wtforms.fields.IntegerField): The weight field instance.
    """
    if field.data > 30:
        raise wtforms.validators.ValidationError("Weight is very big")


class LuggageForm(flask_wtf.FlaskForm):
    """
    Form for luggage registration including weight validation.
    """

    surname = wtforms.StringField(
        "Surname", validators=[wtforms.validators.InputRequired()]
    )
    name = wtforms.StringField("Name", validators=[wtforms.validators.InputRequired()])
    pass_id = wtforms.IntegerField(
        "Password #", validators=[wtforms.validators.InputRequired()]
    )
    luggage_weight = wtforms.IntegerField(
        "Weight luggage",
        validators=[wtforms.validators.InputRequired(), is_luggage_weight_valid],
    )
    submit = wtforms.SubmitField("Register")


@app.route("/luggage/", methods=["GET", "POST"])
def luggage():
    """
    Handles GET and POST requests for luggage form.

    Returns:
        str: Success message or rendered template with form errors.
    """
    form = LuggageForm()
    if flask.request.method == "GET":
        return flask.render_template("luggage.html", form=form)
    if form.validate_on_submit():
        return "ok"
    else:
        print(f"[{__name__}] ERROR: {form.errors}")
        return f"{form.errors} - not valid"


app.run(debug=True, port=7000)
