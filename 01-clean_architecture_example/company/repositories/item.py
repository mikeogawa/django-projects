from typing import List, Optional

from django.db.models.query import QuerySet

from api.commons.repositories import BaseRepository
from company.models import Item

class ItemRepository(BaseRepository):

    model_class = Item

    def get_by_name(self, name: str) -> Item:
        try:
            return self.objects.get(name=name)
        except Item.DoesNotExist:
            return None

    def get_by_code(self, code: str) -> Item:
        try:
            return self.objects.get(code=code)
        except Item.DoesNotExist:
            return None

    def filter_in_id_list(self, id_list: List[str]) -> QuerySet:
        return self.objects.filter(id__in=id_list)

    def filter_eq_shop_id(self, id_: str) -> QuerySet:
        return self.objects.filter(shop_id=id_)
