# from curses import BUTTON2_DOUBLE_CLICKED
from flask import Blueprint, jsonify, abort, make_response

# commenting out hard coded data for Book class and books list
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


# ============================== GET /books route ==============================
# commenting out to refactor in the database
# books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# commenting out to refactor in the database
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


# ============================== GET /books/<book_id> route ==============================
# commenting out to refactor in the database

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)
    
#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }



# ============================== Helper function for invalid book and non-existing books ===
# commenting out to refactor in the database

# def validate_book(book_id):
#     try: 
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message": f"book {book_id} invalid"}, 400))
#     for book in books:
#         if book.id == book_id:
#             return book
#     abort(make_response({"message" : f"book {book_id} not found"}, 404))

