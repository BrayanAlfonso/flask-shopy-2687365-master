from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField,FileRequired, FileAllowed

class ProductForm():
    nombre = StringField('Ingrese producto: ',validators=[InputRequired(message="Ojo, El Nombre Esta Vacio")])
    precio = IntegerField('Ingrese precio: ', validators=[InputRequired(message="Ojo, El Precio Esta Vacio"),NumberRange(message="Ojo, Precio Fuera De Rango", min=5000, max=50000)])



class NewProductForm(FlaskForm, ProductForm):
    imagen= FileField(label="Ingrese Una Imagen Del Producto :3", validators=[FileRequired(message="Ojo, Debe Ingresar Un Archivo :3"),FileAllowed(['jpg','png','jpge','jfif'], message="Solo Se Admiten Imagenes")])
    submit = SubmitField('Registrar')


class EditProductForm(FlaskForm, ProductForm):
    submit = SubmitField('Registrar')