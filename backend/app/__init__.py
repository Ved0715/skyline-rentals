from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    from app.routes import auth, main
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp, url_prefix='/api/auth')
    
    # Import models so Flask-Migrate can detect them
    from app import models
    
    return app