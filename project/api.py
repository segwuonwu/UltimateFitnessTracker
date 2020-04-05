# from flask import Flask 
# from flask_sqlalchemy import SQLAlchemy 
# from flask_login import LoginManager

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)

#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_ECHO'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/trackerDb'
#     app.config['SECRET_KEY'] = 'myultimatefitnesstrackersecretkey'
    
#     db.init_app(app)

#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     return app

