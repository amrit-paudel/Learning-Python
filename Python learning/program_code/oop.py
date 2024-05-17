
class Book:
    def __init__( self, title, author, price ):
        self.__title = title
        self.__author = author
        self.__price = price
book = Book( "Book title","Book author",50000 )
print( book.__author ) # can not be accessed, gives error

