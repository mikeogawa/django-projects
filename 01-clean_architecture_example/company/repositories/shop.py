from typing import List, Optional

from django.db.models.query import QuerySet

from api.commons.repositories import BaseRepository
from company.models import Shop

class ShopRepository(BaseRepository):

    model_class = Shop

    def get_by_name(self, name: str) -> Shop:
        try:
            return self.objects.get(name=name)
        except Shop.DoesNotExist:
            return None

    def get_by_code(self, code: str) -> Shop:
        try:
            return self.objects.get(code=code)
        except Shop.DoesNotExist:
            return None

    def filter_in_name(self, name: str) -> QuerySet:
        return self.objects.filter(name__in=name)

    def filter_in_id_list(self, id_list: List[str]) -> QuerySet:
        return self.objects.filter(id__in=id_list)

    def filter_eq_company_id(self, id_: str) -> QuerySet:
        return self.objects.filter(company_id=id_)

    def filter_in_item_id(self, id: str) -> QuerySet:
        return self.objects.filter(items__id=id)

    def bulk_update_shop_id_to_company(self, shops, company):
        return shops.objects.bulk_update(company, 'company')
