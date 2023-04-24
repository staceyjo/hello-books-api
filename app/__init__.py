from flask import Flask


# def create_app(test_config=None):
def create_app():

    app = Flask(__name__)

    # Register Blueprints for Flask to recognize
    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app
