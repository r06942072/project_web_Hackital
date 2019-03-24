from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    #departure, depart_id, destination, dest_id, date, quantity
    departure = StringField('Departure (Washington, DC)',
                           validators=[DataRequired()])
    depart_id = StringField('Depart ID (WAS)',
                        validators=[DataRequired()])
    destination = StringField('Destination (Boston, MA)',
                        validators=[DataRequired()])
    dest_id = StringField('Dest ID (BOS)',
                        validators=[DataRequired()])
    date123 = StringField('Departure Date (03/28/2019)',
                        validators=[DataRequired()])
    quantity = StringField('How many passengers? (2)',
                        validators=[DataRequired()])
    submit = SubmitField('Start Web Scraping!!!')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
