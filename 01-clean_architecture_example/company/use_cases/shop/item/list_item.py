from api.commons import BaseUseCase
from company.repositories import ItemRepository


class ListItem(BaseUseCase):

    def __init__(self):

        self.repository = ItemRepository()

    def execute(self, id_: str):

        return self.repository.filter_eq_shop_id(id_)
