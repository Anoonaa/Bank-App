"""
Basic Registration and Login forms for the Banking Application
"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    """
    Registration form class

    Attributes:
        username: StringField
        email: StringField
        password: PasswordField
        confirm_password: PasswordField
        submit: SubmitField
    """

    username = StringField(
        label="Username", validators=[DataRequired(), Length(min=2, max=20)]
    )

    email = StringField(label="Email", validators=[DataRequired(), Email()])

    password = PasswordField(
        label="Password", validators=[DataRequired(), Length(min=8, max=40)]
    )

    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(), EqualTo(fieldname="password")],
    )

    submit = SubmitField(label="Sign Up")


class LoginForm(FlaskForm):
    """
    Login Form class

    Attributes:
        username: StringField
        password: PasswordField
        remember: BooleanField
        submit: SubmitField
    """

    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=20)]
        )

    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=8, max=40)]
        )

    remember = BooleanField(label="Remember Me")
    submit = SubmitField('Login')
