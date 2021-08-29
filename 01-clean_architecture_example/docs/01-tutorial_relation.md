# Summary

```
[Compnay] ---< [Shop] >---< [Item]

OR

[Compnay] ---< [Shop] ---< [ShopItemRel] >--- [Item]
```

## Model

```py
from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Company(BaseModel):
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)
    class Meta:
        db_table = "company_company"
        unique_together = (('name', 'code'),)
```



## Model Relation

```py
from django.db import models
from api.commons import BaseModel

class Shop(BaseModel):
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)
    company = models.ForeignKey(
        'company.Company',
        db_column='company_id',
        related_name='shops', # Comapny().shops
        related_query_name='shop_id', # Company.objects.filter(shop_id...)
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
        unique_together = (('name', 'code'),)

class Item(BaseModel):
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64)
    class Meta:
        db_table = "company_item"
        unique_together = (('name', 'code'),)

class ShopItemRel(BaseModel):
    shop = models.ForeignKey('company.Shop', db_column='shop_id', on_delete=models.CASCADE)
    item = models.ForeignKey('company.Item', db_column='item_id', on_delete=models.CASCADE)
    class Meta:
        db_table = "company_shop_item_rel"
```

- [on_delete](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
- [related_name, related_query_name](https://thinkami.hatenablog.com/entry/2020/06/14/145912)
- [field をクラスではなく string にした理由](https://stackoverflow.com/questions/18271001/django-recursive-relationship)


## How to Use

```py
shop=Shop(code="a",name="a")
item_a=Item(code="a",name="a")
item_b=Item(code="b",name="b")

# DB 登録
shop.save()
item_a.save()
item_b.save()

# Relation 追加
shop.items.add(item_a,item_b)
shop.items.remove(item_a)

shop.items.all() # <QuerySet [<Item:Item object (...)>]>
```
