import os
from flask import url_for, current_app
from flask_mail import Message
from siteMain import mail
import cloudinary
import cloudinary.uploader

def save_profile_picture(form_picture):
    cloudinary.config(
        cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME'),
        api_key = os.environ.get('CLOUDINARY_API_KEY'),
        api_secret = os.environ.get('CLOUDINARY_API_SECRET')
    )

    upload_result = cloudinary.uploader.upload(
        form_picture,
        folder='profile_pics',
        transformation=[{'width': 150, 'height': 150, 'crop': 'fill', 'gravity': 'face'}]
    )
    
    return upload_result.get('secure_url')


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Requisição para mudança de senha', 
                  sender='noreply@demo.com', 
                  recipients=[user.email])
    msg.body = f'''Para criar uma nova senha entre no seguinte link:
{url_for('users.reset_token', token=token, _external=True)}

Se você não fez essa requisição apenas ignore esse email.
'''
    mail.send(msg)