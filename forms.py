from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class PostForm(Form):
	title = TextField('title', validators=[DataRequired()])
	post = TextField('post', validators=[DataRequired()])