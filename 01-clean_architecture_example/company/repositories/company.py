from typing import Optional

from django.db.models.query import QuerySet

from api.commons.repositories import BaseRepository
from company.models import Company

class CompanyRepository(BaseRepository):

    model_class = Company

    def get_by_name(self, name: str) -> Company:
        try:
            return self.objects.get(name=name)
        except Company.DoesNotExist:
            return None

    def get_by_code(self, code: str) -> Company:
        try:
            return self.objects.get(code=code)
        except Company.DoesNotExist:
            return None

    def filter_in_name(self, name: str) -> QuerySet:
        return self.objects.filter(name__in=name)

    def filter_eq_shop_id(self, id_: str) -> QuerySet:
        return self.objects.filter(shop_id=id_)
