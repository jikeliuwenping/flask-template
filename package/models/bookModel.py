from peewee import *

from package.base.database import flask_db
from package.models.entities.exampleEntities import *
from .shelfModal import *


class BookModel(ModelSchema):

    shelf = Related()
    potentialShelfs = Related()

    class Meta:
        model = Book

    @classmethod
    def getAllBooksWithShelf(cls):
        # one to one
        books = Book.select(Book, Shelf).join(Shelf)
        return BookModel(many=True).dumps(books)

    @classmethod
    def getBooksWithPotentialShelf(cls):
        # many to many
        books = Book.select()
        positions = Position.select()
        shelfs = Shelf.select()

        query = prefetch(books, positions, shelfs)
        return BookModel(many=True, only=("id", "name", "potentialShelfs")).dumps(query)
