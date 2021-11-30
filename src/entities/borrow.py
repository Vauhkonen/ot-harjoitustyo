from datetime import date
import uuid

# Constructor for new product rental
class Borrow():
    def __init__(self, product, borrower, rentdate=date.today(), returndate=None, description=None):
        self.id = str(uuid.uuid4())
        self.product = product
        self.borrower = borrower
        self.rentdate = rentdate
        self.returndate = returndate
        self.description = description
        self.returned = False


"""     Attributes
    product = product that has been borrowed
    borrower = person that has product/item 
    rentdate = rental date. If empty, will be filled current date
    returndate = date when product/item should be returned. Not mandatory.
    description = free description of rental situation
    returned = boolean, where False is not returned and True when product is marked to returned  

"""
