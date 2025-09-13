from flask_wtf import FlaskForm
from flask_wtf.file import FileField, file_allowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from siteMain.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators= [DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators= [DataRequired(), Email()])

    password = PasswordField('Senha', validators= [DataRequired()])
    confirm_password = PasswordField('Confirmar senha', validators= [DataRequired(), EqualTo('password')])

    submit = SubmitField('Cadastrar')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Nome de usuário já cadastrado')
        
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email já registrado')


class LoginForm(FlaskForm):

    email = StringField('Email', validators= [DataRequired(), Email()])

    password = PasswordField('Senha', validators= [DataRequired()])

    remember = BooleanField('Lembrar de mim')

    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = StringField('Nome de usuário', validators= [DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators= [DataRequired(), Email()])

    picture = FileField('Atualizar foto de perfil', validators=[file_allowed(['jpg', 'png', 'webp'])])

    submit = SubmitField('Atualizar')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('Já existe alguém com esse nome de usuário')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('Email já registrado')
            

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    content = TextAreaField('Conteúdo', validators=[DataRequired()])
    submit = SubmitField('Postar')
    picture = FileField('Postar Imagem', validators=[file_allowed(['jpg', 'png', 'jpeg'])])

