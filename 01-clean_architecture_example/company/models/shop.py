from django.db import models
from api.commons import BaseModel

class Shop(BaseModel):
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)

    company = models.ForeignKey(
        'company.Company',
        db_column='company_id',
        related_name='shops',
        related_query_name='shop_id',
        null=True,
        on_delete=models.CASCADE,
    )

    items = models.ManyToManyField(
        'company.Item',
        related_name='shops',
        related_query_name='shop_id',
        through='company.ShopItemRel',
        )

    class Meta:
        db_table = "company_shop"
        unique_together = (
            ('name', 'code'),
        )
