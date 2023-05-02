# from the main app directory, give the file access to the SQLAlchemy db

from app import db

# define the Book class and name it after the model (usually singular) 
# follow the SQLAchemy pattern for creating a class for the model
# Connect the model with our SQL database

#  (db.Model) The class Book inherits from db.Model from SQLAlchemy
# this allows Flask to work with Model instances (OOP)
# which then allows us to access instance of Model that correspond to a db row
# SQLAlchemy will use the lowercase version of this class name as the name of the table it will create.
class Book(db.Model):

    # map attributes to table columns
    # id = db.() instances of Book will have an attribute id, 
    # which will map to a database column.
    # db.Integer is a column data-type that SQL Alchemy defines & stores
    # primary_key and autoincrement are keywrod arguments that allow SQLAlchemy to understand how to fill in the values for new Book instances.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # title = ... creates an attribute, which will map to a string column, title
    title = db.Column(db.String)

    # description = ... creates an attribute, which will map to a string column, description
    description = db.Column(db.String)
    
    # to create a different table namein the db,  other than the singular class name
    # __tablename__ = "books"
    
    # could add functions here just like any class
    def to_string(self):
        return f"{self.id}: {self.title} Description:  {self.description}"