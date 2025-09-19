from flask import (Blueprint, abort, request, redirect, flash, url_for, render_template, current_app)
from flask_login import current_user, login_required
from siteMain import db
from siteMain.models import Post
from siteMain.posts.forms import PostForm
import os


import cloudinary
import cloudinary.uploader

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post_image_url = None

        if form.picture.data:
            post_image_url = save_post_picture(form.picture.data)


        post = Post(title=form.title.data, 
                    content=form.content.data, 
                    author=current_user,
                    image_file=post_image_url, 
                    is_pinned=form.is_pinned.data if hasattr(form, 'is_pinned') else False) 
        db.session.add(post)
        db.session.commit()
        flash('Sua postagem foi criada!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Nova Postagem',
                            form=form, legend = 'Nova Postagem')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['POST', 'GET'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_url = save_post_picture(form.picture.data)
            post.image_file = picture_url

        post.title = form.title.data
        post.content = form.content.data
        if hasattr(form, 'is_pinned'):
            post.is_pinned = form.is_pinned.data
        db.session.commit()
        flash('Sua postagem foi atualizada!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        if hasattr(form, 'is_pinned'):
            form.is_pinned.data = post.is_pinned
    return render_template('create_post.html', title='Atualizar Postagem', 
                           form=form, legend='Atualizar Postagem')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
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
    

    cloudinary.config(
        cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME'),
        api_key = os.environ.get('CLOUDINARY_API_KEY'),
        api_secret = os.environ.get('CLOUDINARY_API_SECRET')
    )


    upload_result = cloudinary.uploader.upload(
        form_picture,
        folder='post_pics', 
        transformation=[{'width': 800, 'height': 800, 'crop': 'limit'}] 
    )
    
    
    return upload_result.get('secure_url')