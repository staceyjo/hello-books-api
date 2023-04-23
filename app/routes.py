from flask import Blueprint

# Blueprint is a Flask class that provides a pattern for grouping 
# related routes (endpoints). Flask will often refer to these routes 
# using the word "view" due to Flask having the potential of sending HTML views.
# However, we will be sending back JSON.
hello_world_bp = Blueprint("hello_world", __name__)


# ================================= endpoint 1 ===============================
# This decorator transforms the function that follows into an endpoint. 
# We use the .route() instance method from our Blueprint instance.

#  Together these arguments define what type of request will be routed to this function. 
# The first argument defines the path (or URL) of the request and the second argument defines a list of HTTP methods (or verbs) the request could have.
# @blueprint_name.route("/endpoint/path/here", methods=["GET"])
@hello_world_bp.route("/hello-world", methods=["GET"])


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
def say_hello_world():
    
    my_beautiful_response_body = "Hello, World!"
    
    return my_beautiful_response_body


# ================================= endpoint 2 ===============================

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    
# ================================= endpoint 3 ===============================

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body