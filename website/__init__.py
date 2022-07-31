from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

# initialize Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwertyuiop' # encrypt/secure cookies and session data
    app.run(host='0.0.0.0', port=80)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # my sql database is located the 'website' folder. f string - when you put f beforehand you can use the squiggly brackets {}
    db.init_app(app)

    #import our blueprints
    from .views import views
    from .auth import auth

    #register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #where should flask redirect us if we're not logged in
    login_manager.init_app(app)

    @login_manager.user_loader #login manager function, that is indicating how we load a user 
    def load_user(id):
        return User.query.get(int(id)) #by default it looks for the primary key(id) and check if it matches with what we pass (in this case, int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database !')