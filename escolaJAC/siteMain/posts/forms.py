from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    content = TextAreaField('Conteúdo', validators=[DataRequired()])
    submit = SubmitField('Postar')
    is_pinned = BooleanField('Fixar este anúncio?') 
    picture = FileField('Postar Imagem', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])