from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(message='Campo obrigatório')])
    content = TextAreaField('Conteúdo', validators=[DataRequired('Campo obrigatório')])
    submit = SubmitField('Postar')
    is_pinned = BooleanField('Fixar este anúncio?') 
    picture = FileField('Postar Imagem', validators=[FileAllowed(['jpg', 'png', 'jpeg'], message='Selecione apenas arquivos suportados')])