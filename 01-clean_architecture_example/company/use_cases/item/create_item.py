from typing import Dict
from company.repositories import ItemRepository
from api.commons import exceptions
from api.commons import BaseUseCase

class CreateItem(BaseUseCase):

    def __init__(self):

        self.repository = ItemRepository()

    def execute(self, data: Dict[str, str]):

        obj = self.repository.get_by_code(data["code"])

        if obj:
            raise exceptions.ConflictError({'code': 'Conflict'})

        obj = self.repository.create(data)
        
        return obj
