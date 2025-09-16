from flask import (Blueprint, request, redirect, flash, url_for, render_template)
from flask_login import current_user, login_required, logout_user, login_user
from siteMain import db, bcrypt, app
from siteMain.models import Post, User
from siteMain.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm, ResquestResetForm, ResetPasswordForm)
from siteMain.users.utils import save_picture, send_reset_email
import os



users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Conta criada com sucesso!', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', title = 'Registrar', form=form)

@users.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Algo deu errado, cheque o email ou a senha', 'danger')
    return render_template('login.html', title = 'Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            old_pic = current_user.image_file
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            if old_pic != 'default.jpg':
                os.remove(os.path.join(app.root_path, 'static/profile_pics', old_pic))
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Sua conta foi atualizada!", 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Conta', image_file = image_file, form = form)



@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author = user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page = page, per_page=8)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = ResquestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        send_reset_email(user)
        flash('Foi enviado um email com instruções para mudança de senha', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title = 'Resetar senha', form = form)



@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash ('Token invalido ou expirado', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Senha atualizada com sucesso!', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title = 'Resetar senha', form = form)