from entities.borrow import Borrow
from repositories.rent_repository import repository

class Service:
    def __init__(self) -> None:
        self._repository = repository

    # Takes list and creates borrow-object
    def create_borrow(self, record):

        product = record[0]
        borrower = record[1]
        rentdate = record[2]
        returndate = record[3]
        description = record[4]

        borrow = Borrow(product, borrower, rentdate, returndate, description)

        return self._repository.save_new(borrow)


service = Service()