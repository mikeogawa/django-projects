## QuerySet

```py
python manage.py shell
from company.models import Company
c=Company(name="cat house",code="")
c.save()
Company.objects.all()
Company.objects.first() # c と同じ
Company.objects.exists()
Company.objects.order_by("name")
Company.objects.get(name="cat house") # attribute を引数に指定
Company.objects.filter(name="cat house") 
Company.objects.filter(name__in=["cat"]) # 特定の集合体に含む場合は __in を追加
Company.objects.filter(name__contains="cat") # attrbuteが文字を含むにしたい場合は __contains を追加
Company.objects.filter(shop_id__name="cat shop") # relation 系も可能
```

Note: iterator になるまでは Query 実行しない

[その他](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)