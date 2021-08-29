# Clean Architecture


[Django Design](https://stackoverflow.com/questions/42037633/django-and-domain-driven-design)

- layer を分離する
- request は内側に向き、response は外側に一方的に向くような実装であること

## サンプルコード

```py
from abc import ABC, abstractmethod

from restframework import views
from rest_framework.response import Response

from company.models import Company

class BaseRepository(ABC):
    @abstractmethod
    def list(self):
        pass
    @abstractmethod
    def get(self, id):
        pass
    
class Repository(BaseRepository):
    """
    All objects(queryset) process goes here
    """
    def list(self):
        return Company.objects.list()
    def get(self, id):
        return Company.objects.get(id)
    .....

class CompanySerializer(serializer.ModelSerializer):
    class Meta:
        model=Company
        fields=__all__

class GetCompany:
    """
    All the business logics go here
    """
    def __init__(self, repository:BaseRepository):
        self.repository = repository
    def execute(self, id_:str):
        return self.repository.get(id_)

class CompanyView(views.ViewSet):
    """
    Only Process Validation And Usecase
    """
    ....
    def retrieve(self, request, id):

        repository = Repository()
        usecase = GetCompany(repository)

        data = usecase.execute(id)

        serializer = CommentSerializer(comment)
        return Response(serializer.data)
```

## QuerySet (Manager) で十分では?
しかし、下記のようにQuerySet(Manager)だけで十分という話もある：
https://www.reddit.com/r/django/comments/d0596f/orm_vs_orm_repository_pattern/
https://note.com/cyberz_cto/n/n26f535d6c575

ではどちらがいいか？

以下を例に
```
Company ---< Shop >---< Item
```

という relation があったとする

## Repository 実装するメリットデメリット
メリット
- Clean Architecture ぽい -> 理解しやすい

デメリット
- objects の query の組み合わせに応じて、メソッドを追加しないといけない

```py
class Repository:
    def filter_in_name_list(self,name_list:List[str]):
        Company.objects.filter(name__in=name_list)
    def filter_in_name_list_and_select_related_shop(self,name_list:List[str]):
        Company.objects.select_related("shop").filter(name__in=name_list)
    ....

# やりたいこと
r = Repository()
r.filter_in_name_list(name_list:List)
r.filter_in_name_list_and_select_related_shop(name_list)
```

## QuerySet実装するメリット・デメリット
メリット
- チェーン実装ができる
```py
class CompanyQueySet(QuerySet):
    def select_related_shop(self):
        return self.select_related("shop")

    def filter_in_name(self, name_list):
        return self.filter(name__in=name_list)

class Company:
    ...
    objects = CompanyQueySet.as_manager()

# やりたいこと
Company.objects.filter_in_name()
Company.objects.select_related_shop().filter_in_name()
```

デメリット
- Clean？と疑う人もいる (objects が剥き出しになって気持ち悪い)