from typing import Optional

from django.db.models.query import QuerySet

from api.commons.repositories import BaseRepository
from company.models import User

class UserRepository(BaseRepository):

    model_class = User

    def get_by_username(self, username: str) -> Optional[User]:
        try:
            return self.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def get_by_email(self, username: str) -> Optional[User]:
        try:
            return self.objects.get(email=username)
        except User.DoesNotExist:
            return None

    def filter_in_name(self, username: str) -> QuerySet:
        return self.objects.filter(username__in=username)

    def filter_in_email(self, username: str) -> QuerySet:
        return self.objects.filter(email__in=username)