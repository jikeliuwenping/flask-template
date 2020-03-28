from package.models.bookModel import *


class BookService():

    @classmethod
    def getAllBooksWithShelf(cls):
        return BookModel.getAllBooksWithShelf()

    @classmethod
    def getBooksWithPotentialShelf(cls):
        return BookModel.getBooksWithPotentialShelf()
