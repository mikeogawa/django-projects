from typing import Dict
from company.repositories import ItemRepository
from api.commons import (
    BaseUseCase,
)

class DeleteItem(BaseUseCase):

    def __init__(self):

        self.repository = ItemRepository()

    def execute(self, id: str):

        obj = self.repository.get_by_id(id)

        if obj:
            obj.delete()

