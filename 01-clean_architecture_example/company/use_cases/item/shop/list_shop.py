from api.commons import BaseUseCase
from company.repositories import ShopRepository


class ListShop(BaseUseCase):

    def __init__(self):

        self.shop_repository = ShopRepository()

    def execute(self, id_: str):
        return self.shop_repository.filter_in_item_id(id_)
