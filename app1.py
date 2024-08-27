import flask
import flask_wtf
import wtforms


class SubcriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('Name')
    email = wtforms.StringField('Email')
    color = wtforms.ColorField('Color')
    submit = wtforms.SubmitField('Send')


class IcecreamForm(flask_wtf.FlaskForm):
    tastes = wtforms.SelectField('Tastes')
    topping = wtforms.SelectMultipleField('Topping')
    cup_size = wtforms.RadioField('Cup size')
    submit = wtforms.SubmitField('Send')


class CarsForm(flask_wtf.FlaskForm):
    model = wtforms.SelectField('Models')
    price = wtforms.IntegerField('Price')
    gearbox = wtforms.RadioField('Gearbox')
    color = wtforms.ColorField('Color')
    submit = wtforms.SubmitField('Send')


class RegistrationForm(flask_wtf.FlaskForm):
    email = wtforms.StringField('Email')
    password = wtforms.PasswordField('Password')
    submit = wtforms.SubmitField('Send')
    remember = wtforms.BooleanField('Remember me')


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'ad'


@app.route('/subscribe/', methods=['GET', 'POST'])
def subscribe():
    form = SubcriptionForm()
    if flask.request.method == 'GET':
        return flask.render_template('subscribe.html', form=form)
    return form.name.data


@app.route('/ice/', methods=['GET', 'POST'])
def ice():
    form = IcecreamForm()
    form.tastes.choices = [
        ('vanila', 'vanila'), ('choko', 'choko'), ('mango', 'mango'), ('lemon', 'banan')]
    form.topping.choices = [('coffee', 'coffee'), ('strawberry', 'strawberry')]
    form.cup_size.choices = [('little', 'little'),
                             ('medium', 'medium'), ('big', 'big')]

    if flask.request.method == 'GET':
        return flask.render_template('ice.html', form=form)
    return form.tastes.data


@app.route('/cars/', methods=['GET', 'POST'])
def cars():
    form = CarsForm()
    form.model.choices = [('Audi', 'Audi'), ('BMW', 'BMW'), ('Tesla', 'Tesla')]
    form.gearbox.choices = [('Auto', 'Auto'), ('Manual', 'Manual')]

    if flask.request.method == 'GET':
        return flask.render_template('cars.html', form=form)
    return form.model.data


@app.route('/register/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()

    if flask.request.method == 'GET':
        return flask.render_template('registration.html', form=form)
    return form.email.data


app.run(debug=True, port=3000)
