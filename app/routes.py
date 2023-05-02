# from os import abort

# import modules
# db is our connection to the database
from app import db

# importing the Book model
from app.models.book import Book

# import dependencies
from flask import Blueprint, jsonify, abort, make_response, request

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]


# creating the Blueprint instance to group all routes that 
# start with /books
# "books" is the debugging name for this Blueprint
# __name__ provides information the blueprint uses for certain aspects of routing
# url_prefix="/books" is a keyword argument that indicates that every endpoint 
# using this Blueprint should be treated like it starts with /books.
# books_bp = Blueprint("books_bp", __name__, url_prefix="/books")
books_bp = Blueprint("books", __name__, url_prefix="/books")

# decorator that uses the books_bp Blueprint to define an endpoint 
# and accepted HTTP method. 
@books_bp.route("", methods=["POST"])

# The function after the decorator will execute whenever a 
# matching HTTP request is received.
def handle_books():
    
    # request_body variable holds the body contents of the HTTP request 
    # in a Python data structure
    request_body = request.get_json()
    
    # error checking/ input validation
    # fixes 500 internal error for invalid request
    if "title" not in request_body or "description" not in request_body:
        return make_response("Invalid request", 400)
    
    # creates a variable to hold the new instance of Book using the data in request_body. 
    # title = & description = are keyword arguments that match our model attributes, 
    # and access the request_body values to create the Book instance
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    # the database's way of collecting changes(add(new_book)) that need to be made
    db.session.add(new_book)
    
    # database to save and commit the collected changes.
    db.session.commit()

    # explicitly return the HTTP response for the endpoint
    # make_response instantiates a Response object
    # (parameter) is the HTTP response body as a string, 
    # unless we have more specific requirements
    # 201 response code, 200 is the default
    return make_response(f"Book {new_book.title} successfully created", 201)
    
    # can also return the response implicitly as a tuple:
    # and return default 200 status code
    # return f"Book {new_book.title} successfully created"


#def validate_book(book_id):
#    try:
#        book_id = int(book_id)
#    except:
#        abort(make_response({"message":f"book {book_id} invalid"}, 400))
#
#    for book in books:
#        if book.id == book_id:
#            return book
#
#    abort(make_response({"message":f"book {book_id} not found"}, 404))
        

# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return jsonify(books_response)

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)
#
#     return {
#           "id": book.id,
#           "title": book.title,
#           "description": book.description,
#     }

