from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField
from wtforms.validators import InputRequired, NumberRange


class LoginForm(FlaskForm):
    username = StringField('Ingrese su nombre de usuario: ',validators=[InputRequired(message="Nombre requerido")])
    password = PasswordField('Ingrese su contraseña: ', validators=[InputRequired(message="Contraseña requerida")])
    submit = SubmitField("Iniciar sesión")
