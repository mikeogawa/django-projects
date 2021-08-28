from api.commons import BaseModel
from django.db import models

class User(BaseModel):

    username = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    companies = models.ForeignKey(
        'company.Item',
        related_name='users',
        related_query_name='user',
        on_delete=models.CASCADE,
        )

    class Meta:
        db_table = "company_user"