from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,Length

class SignupForm(FlaskForm):
    first_name = StringField("First_Name",validators=[DataRequired("Please Enter Your First Name")])
    last_name = StringField("Last_Name",validators=[DataRequired("Please Enter Your  Last Name")])
    email = StringField("Email",validators=[DataRequired,Email("Please Enter Your Email")])
    password = PasswordField("Password",validators=[DataRequired("Please Enter Your Password"),Length(min=6,message="Password Must Be minimum Characters")])
    submit = SubmitField("Sign Up")

