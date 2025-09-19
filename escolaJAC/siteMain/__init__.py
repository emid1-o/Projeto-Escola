from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from siteMain.config import Config
from dotenv import load_dotenv
load_dotenv()




db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
migrate = Migrate()






def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)


    @app.context_processor
    def inject_pinned_posts():
        
        try:
            pinned_posts = Post.query.filter_by(is_pinned=True).order_by(Post.date_posted.desc()).limit(5).all()
            return dict(pinned_posts=pinned_posts)
        except:
            return dict(pinned_posts=[])


    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)


    from siteMain.users.routes import users
    from siteMain.posts.routes import posts
    from siteMain.main.routes import main
    from siteMain.errors.handlers import errors
    from siteMain.models import Post
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
