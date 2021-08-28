from typing import Optional, List

from django.db.models.query import QuerySet

from api.commons.repositories import BaseRepository
from company.models import ShopItemRel

class ShopItemRelRepository(BaseRepository):

    model_class = ShopItemRel

    def filter_by_shop_id(self, id_: str) -> QuerySet:
        return self.objects.filter(shop_id=id_)

    def filter_by_item_id(self, id_: str) -> QuerySet:
        return self.objects.filter(item_id=id_)
