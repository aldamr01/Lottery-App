from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, EmailField


class LoginForm(FlaskForm):
    email = EmailField(
        "Email", [validators.Length(min=4, max=50), validators.DataRequired()]
    )
    password = PasswordField(
        "Password",
        [validators.Length(min=6, max=200), validators.DataRequired()],
    )
    
class RegisterForm(FlaskForm):
    name = StringField(
        "Name", [validators.Length(min=4, max=50), validators.DataRequired()]
    )
    password = PasswordField(
        "Password",
        [validators.Length(min=6, max=200), validators.DataRequired()],
    )
    email = EmailField(
        "Email", [validators.Length(min=4, max=50), validators.DataRequired()]
    )