from typing import Dict
from company.repositories import ShopRepository
from api.commons import exceptions
from api.commons import BaseUseCase

class CreateShop(BaseUseCase):

    def __init__(self):

        self.repository = ShopRepository()

    def execute(self, data: Dict[str, str]):

        obj = self.repository.get_by_code(data["code"])

        if obj:
            raise exceptions.ConflictError({'code': 'Conflict'})

        obj = self.repository.create(data)
        
        return obj
