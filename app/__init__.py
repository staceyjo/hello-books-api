from flask import Flask
from flask import Blueprint

# This decorator transforms the function that follows into an endpoint. 
# We use the .route() instance method from our Blueprint instance.

#  Together these arguments define what type of request will be routed to this function. 
# The first argument defines the path (or URL) of the request and the second argument defines a list of HTTP methods (or verbs) the request could have.
# @blueprint_name.route("/endpoint/path/here", methods=["GET"])

# This function will execute whenever a request that matches the decorator is received. 
# The function can be named whatever feels most appropriate.
# def endpoint_name():

    # We must define a response body to return. 
    # Here, we're using a local variable my_beautiful_response_body to hold a value
#     my_beautiful_response_body = "Hello, World!"
    # For each endpoint, we must return the HTTP response.
    # Give a response 200 OK with the HTTP body "Hello, World!"
    #  If we don't set the status code ourselves, Flask will use 200 OK by default.

    # return my_beautiful_response_body



hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("ç", methods=["GET"])

def say_hello_world():
    
    my_beautiful_response_body = "Hello, World!"
    
    return my_beautiful_response_body


def create_app(test_config=None):
    app = Flask(__name__)
    
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app