from company.repositories import ShopRepository
from api.commons import BaseUseCase

class ListShop(BaseUseCase):

    def __init__(self):

        self.repository = ShopRepository()

    def execute(self):

        return self.repository.list()
