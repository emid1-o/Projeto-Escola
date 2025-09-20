from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from siteMain.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', 
                           validators=[DataRequired(message='Este campo é obrigatório.'), 
                                       Length(min=2, max=20, message='O nome de usuário deve ter entre 2 e 20 caracteres.')])

    email = StringField('Email', 
                        validators=[DataRequired(message='Este campo é obrigatório.'), 
                                    Email(message='Por favor, insira um endereço de e-mail válido.')])

    password = PasswordField('Senha', 
                             validators=[DataRequired(message='Este campo é obrigatório.')])
    
    confirm_password = PasswordField('Confirmar senha', 
                                     validators=[DataRequired(message='Este campo é obrigatório.'), 
                                                 EqualTo('password', message='As senhas não coincidem.')])

    registration_key = StringField('Chave de Registro', 
                                   validators=[DataRequired(message='A chave de registro é obrigatória.')])

    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este nome de usuário já está em uso. Por favor, escolha outro.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este e-mail já está em uso. Por favor, escolha outro.')


class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(message='Este campo é obrigatório.'), 
                                    Email(message='Por favor, insira um endereço de e-mail válido.')])

    password = PasswordField('Senha', 
                             validators=[DataRequired(message='Este campo é obrigatório.')])

    remember = BooleanField('Lembrar de mim')

    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Nome de usuário', 
                           validators=[DataRequired(message='Este campo é obrigatório.'), 
                                       Length(min=2, max=20, message='O nome de usuário deve ter entre 2 e 20 caracteres.')])

    email = StringField('Email', 
                        validators=[DataRequired(message='Este campo é obrigatório.'), 
                                    Email(message='Por favor, insira um endereço de e-mail válido.')])

    picture = FileField('Atualizar foto de perfil', 
                        validators=[FileAllowed(['jpeg','jpg', 'png', 'webp'], message='Apenas arquivos de imagem (.jpeg, .jpg, .png, .webp) são permitidos.')])

    submit = SubmitField('Atualizar')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Este nome de usuário já está em uso. Por favor, escolha outro.')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Este e-mail já está em uso. Por favor, escolha outro.')
            
class ResquestResetForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(message='Este campo é obrigatório.'), 
                                    Email(message='Por favor, insira um endereço de e-mail válido.')])
    submit = SubmitField('Mudar senha')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Não há nenhuma conta registrada com este e-mail.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Senha', 
                             validators=[DataRequired(message='Este campo é obrigatório.')])
    
    confirm_password = PasswordField('Confirmar senha', 
                                     validators=[DataRequired(message='Este campo é obrigatório.'), 
                                                 EqualTo('password', message='As senhas não coincidem.')])
    
    submit = SubmitField('Resetar senha')