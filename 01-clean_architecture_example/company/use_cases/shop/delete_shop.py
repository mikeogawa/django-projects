from typing import Dict
from company.repositories import ShopRepository
from api.commons import (
    BaseUseCase,
)

class DeleteShop(BaseUseCase):

    def __init__(self):

        self.repository = ShopRepository()

    def execute(self, id: str):

        obj = self.repository.get_by_id(id)

        if obj:
            obj.delete()

