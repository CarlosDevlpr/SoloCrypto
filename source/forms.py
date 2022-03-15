import email
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from source.models import User
from flask_login import current_user

class FormCreateAccount(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(6,20)])
    confirm_password = PasswordField('Confirm your Password: ', validators=[DataRequired(), EqualTo('password')])
    submit_create_account = SubmitField('Create Account')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email already registered, Register with another email or login to continue')

class FormLogin(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(6,20)])
    remember_me = BooleanField('Remember Me')
    SubmitField('Login')
