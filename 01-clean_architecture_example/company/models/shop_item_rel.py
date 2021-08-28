from django.db import models
from api.commons import BaseModel

class ShopItemRel(BaseModel):
    shop = models.ForeignKey('company.Shop', db_column='shop_id', on_delete=models.CASCADE)
    item = models.ForeignKey('company.Item', db_column='item_id', on_delete=models.CASCADE)

    class Meta:
        db_table = "company_shop_item_rel"