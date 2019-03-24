from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    #departure, depart_id, destination, dest_id, date, quantity
    departure = StringField('Departure (Washington, DC)')
    depart_id = StringField('Depart ID (WAS)')
    destination = StringField('Destination (Boston, MA)')
    dest_id = StringField('Dest ID (BOS)')
    date123 = StringField('Departure Date (03/28/2019)')
    quantity = StringField('How many passengers? (2)')
    submit = SubmitField('Start Web Scraping!!!')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
