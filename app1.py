"""
A simple Flask application with multiple forms for different use cases.
"""

import flask
import flask_wtf
import wtforms


class SubscriptionForm(flask_wtf.FlaskForm):
    """Form for subscription with name, email, and color fields."""

    name = wtforms.StringField("Name")
    email = wtforms.StringField("Email")
    color = wtforms.ColorField("Color")
    submit = wtforms.SubmitField("Send")


class IcecreamForm(flask_wtf.FlaskForm):
    """Form for selecting ice cream flavors and toppings."""

    tastes = wtforms.SelectField("Tastes")
    topping = wtforms.SelectMultipleField("Topping")
    cup_size = wtforms.RadioField("Cup size")
    submit = wtforms.SubmitField("Send")


class CarsForm(flask_wtf.FlaskForm):
    """Form for selecting car models and specifications."""

    model = wtforms.SelectField("Models")
    price = wtforms.IntegerField("Price")
    gearbox = wtforms.RadioField("Gearbox")
    color = wtforms.ColorField("Color")
    submit = wtforms.SubmitField("Send")


class RegistrationForm(flask_wtf.FlaskForm):
    """Form for user registration with email and password fields."""

    email = wtforms.StringField("Email")
    password = wtforms.PasswordField("Password")
    submit = wtforms.SubmitField("Send")
    remember = wtforms.BooleanField("Remember me")


app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "ad"


@app.route("/subscribe/", methods=["GET", "POST"])
def subscribe():
    """Handle subscription form submission."""
    form = SubscriptionForm()
    if flask.request.method == "POST":
        return form.name.data
    return flask.render_template("subscribe.html", form=form)


@app.route("/ice/", methods=["GET", "POST"])
def ice():
    """Handle ice cream form submission."""
    form = IcecreamForm()
    form.tastes.choices = [
        ("vanilla", "Vanilla"),
        ("choco", "Choco"),
        ("mango", "Mango"),
        ("banana", "Banana"),
    ]
    form.topping.choices = [("coffee", "Coffee"), ("strawberry", "Strawberry")]
    form.cup_size.choices = [("little", "Little"), ("medium", "Medium"), ("big", "Big")]

    if flask.request.method == "POST":
        return form.tastes.data
    return flask.render_template("ice.html", form=form)


@app.route("/cars/", methods=["GET", "POST"])
def cars():
    """Handle car form submission."""
    form = CarsForm()
    form.model.choices = [("Audi", "Audi"), ("BMW", "BMW"), ("Tesla", "Tesla")]
    form.gearbox.choices = [("Auto", "Auto"), ("Manual", "Manual")]

    if flask.request.method == "POST":
        return form.model.data
    return flask.render_template("cars.html", form=form)


@app.route("/register/", methods=["GET", "POST"])
def registration():
    """Handle user registration form submission."""
    form = RegistrationForm()

    if flask.request.method == "POST":
        return form.email.data
    return flask.render_template("registration.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
