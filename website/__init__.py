from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__) # inicialize the name of the file
  app.config['SECRET_KEY'] = 'thisIsSecretKey'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #my sqlalchemy is stored at this location
  db.init_app(app) # this is the app we're gonna use for this database

  from .views import views
  from .auth import auth
  app.register_blueprint(views, url_prefix = '/') # all of the URLs that are stored inside the blueprint file, there's no prefix (since we did not do something like /auth/. If we did, we need to go to /auth/whatever inside the auth.route)
  app.register_blueprint(auth, url_prefix = '/')

  from .models import User, Note
  # create_database(app)
  with app.app_context():
    db.create_all()
   
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login' # the place a user should go when he/she's not logged in
  login_manager.init_app(app) # tell login_manager which app we're using

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))
  # this is telling flask how we load a user
  # similar to filter, but when we use get, it's looking for primary key by default, no need to specift id = id
    
  return app

# def create_database(app):
#   if not path.exists('website/' + DB_NAME):
#     db.create_all(app=app)
#     print('Created Database!')