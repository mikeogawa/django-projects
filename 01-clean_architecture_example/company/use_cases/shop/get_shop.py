from api.commons import exceptions
from api.commons import BaseUseCase
from company.repositories import ShopRepository

class GetShop(BaseUseCase):

    def __init__(self):

        self.repository = ShopRepository()

    def execute(self, id: str):

        obj = self.repository.get_by_id(id)

        if obj is None:
            raise exceptions.NotFound({'id': 'Not found'})

        return obj
