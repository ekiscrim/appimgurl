from flask import Blueprint, render_template,request
from models.formRegistro import FormRegistro

mod = Blueprint('core',__name__, template_folder='templates') #el nombre que recibe 
@mod.route('/')
def index():
	return  render_template('index.html')

# deberia dividr todos estos aparte, hacer blueprint para cada uno, login, registro...y sacarlo a vistas distintas
@mod.route('/login')
def login():
	return 'login'

@mod.route('/registro')
def registro_get():
	formulario = FormRegistro()
	return  render_template('registro.html', form=formulario)

@mod.route('/registro', methods=['GET','POST'])
def registro():
	formulario = FormRegistro()
	if request.method == 'POST':
		if formulario.validate_on_submit():
			return  render_template('registro.html', form=formulario, valido=True)
		return  render_template('registro.html', form=formulario)
@mod.route('/logout')
def logout():
	return  'salir'
