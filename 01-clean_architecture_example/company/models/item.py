from django.db import models
from api.commons import BaseModel

class Item(BaseModel):
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "company_item"
        unique_together = (
            ('name', 'code'),
        )