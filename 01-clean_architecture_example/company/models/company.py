from django.db import models
from api.commons import BaseModel

class Company(BaseModel):

    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = "company_company"
        unique_together = (
            ('name', 'code'),
        )