from flask.ext.wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class FormRegistro(Form):
	nick = StringField('nick', validators=[DataRequired()])
	passw = PasswordField('pass', validators=[DataRequired()])
	submit = SubmitField('registro')