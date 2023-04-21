from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK-MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "... some path to Postgres Database"
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # import models (data objects) here
    
    return app