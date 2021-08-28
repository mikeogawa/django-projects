from typing import List
from company.repositories.company import CompanyRepository
from api.commons import exceptions
from api.commons import BaseUseCase
from company.repositories import (
    ItemRepository,
    ShopRepository,
)


class ConnectItem(BaseUseCase):

    def __init__(self):

        self.shop_repository = ShopRepository()
        self.item_repository = ItemRepository()

    def execute(self, shop_id: str, item_ids: List[str]):

        shop = self.shop_repository.get_by_id(shop_id)

        if shop is None:
            raise exceptions.NotFound()

        items = self.item_repository.filter_in_id_list(item_ids)

        shop.items.add(*list(items))

        return [str(s.id) for s in items]
