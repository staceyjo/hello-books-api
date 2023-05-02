# -- Configure the database to use SQLAlchemy in app/__init__.py
# The __init__.py serves double duty: 
# it will contain the application factory, and 
# it tells Python that the app directory should be treated as a package.

# import packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# set up variables for database operations
# set db to an SQLAlchemy object to use it to interact with the db
db = SQLAlchemy()
# create a migrate object which we will use when we need to change the structure of the db
migrate = Migrate()

# Flask application is an instance of the Flask class
# Create the Flask application inside a "application factory" funciton
# create_app() function takes a config argument from our config.py file
# if one exists
def create_app(test_config=None):
    # Create an app variable and initialize/create an instance of Flask
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    # set up database by configuring the app to include SQLAlchemy settings: 
        # app.config key 1--set to False to hide a warning about a feature in SQLAlchemy
        # If set to True, Flask-SQLAlchemy will track modifications of objects and emit signals. 
        # The default is None, which enables tracking but issues a warning that it will be disabled 
        # by default in the future. 
        # This requires extra memory and should be disabled if not needed, so we set to False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
        # app.config key 2 --sets the database URI that should be used for the connection
        # by setting the connection string for our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
    
    
    # initialize SQLAlchemy object(db) and pass in the application 
    # initialize migrate object (migrate) to connect db to our flask app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # import the model to make it available to the app when we update the db
    from app.models.book import Book

    # import routes for blueprint
    # from .routes import books_bp
    
    # register the blueprint
    # app.register_blueprint(books_bp)



    # return the application
    return app