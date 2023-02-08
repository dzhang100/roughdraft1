from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# database = SQLAlchemy()
# database_name = 'database.db'

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_name}'
    # database.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    #imports user and notes from database
    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    with app.app_context():
        db.create_all()



    return app

# def create_database(app):
#     if not path('website/' + database_name):
#         database.create_all(app=app)
#         print('Created Database!')
