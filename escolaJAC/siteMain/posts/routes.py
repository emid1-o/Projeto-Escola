from flask import (Blueprint, abort, request, redirect, flash, url_for, render_template, current_app)
from flask_login import current_user, login_required
from siteMain import db
from siteMain.models import Post
from siteMain.posts.forms import PostForm
from PIL import Image
import os
import secrets

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post_image = None
        if form.picture.data:
            picture_file = save_post_picture(form.picture.data)
            post_image = picture_file

        post = Post(title=form.title.data, 
                    content=form.content.data, 
                    author=current_user,
                    image_file=post_image,
                    is_pinned=form.is_pinned.data) 
        db.session.add(post)
        db.session.commit()
        flash('Sua postagem foi criada!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Nova Postagem',
                            form=form, legend = 'Nova Postagem')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title = post.title, post = post)


@posts.route("/post/<int:post_id>/update", methods = ['POST', 'GET'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():

        if form.picture.data:
            
            picture_file = save_post_picture(form.picture.data)
        
            post.image_file = picture_file

        post.title = form.title.data
        post.content = form.content.data
        post.is_pinned = form.is_pinned.data
        db.session.commit()
        flash('Sua postagem foi atualizada!', 'success')
        return redirect(url_for('posts.post', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.is_pinned.data = post.is_pinned
    return render_template('create_post.html', title='Atualizar Postagem', 
                           form=form, legend = 'Atualizar Postagem')



@posts.route("/post/<int:post_id>/delete", methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Sua postagem foi deletada", 'success')
    return redirect(url_for('main.home'))


def save_post_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/post_pics', picture_fn)

    
    output_size = (600, 600) 
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn