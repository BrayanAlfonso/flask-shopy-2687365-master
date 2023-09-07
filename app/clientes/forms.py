from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired


class ClienteForm(FlaskForm):
    username = StringField('Ingrese su nombre de usuario: ',validators=[InputRequired(message="Ojo, El Nombre Esta Vacio")])
    email = StringField('Ingrese su correo: ',validators=[InputRequired(message="Ojo, El Nombre Esta Vacio")])
    password = StringField('Ingrese su contraseña ',validators=[InputRequired(message="Ojo, El Nombre Esta Vacio")])
    submit = SubmitField('Registrar')


