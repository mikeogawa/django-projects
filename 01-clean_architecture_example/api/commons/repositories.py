from typing import Dict
from django.db import models
from django.db.models.query import QuerySet

class BaseRepository:

    model_class:models.Model

    def list(self) -> QuerySet:
        return self.objects.all()

    def get_by_id(self, id_:str) -> models.Model:
        try:
            return self.objects.get(id=id_)
        except self.model_class.DoesNotExist:
            return None
    
    def create(self, data:Dict[str,str]) -> models.Model:
        obj = self.model_class(**data)
        obj.save()
        return obj

    def update(self, obj: models.Model, data:Dict[str,str]) -> models.Model:
        for k,v in data.items():
            setattr(obj,k,v)
        obj.save()
        return obj

    def delete(self, obj):
        return obj.delete()

    @property
    def objects(self):
        return self.model_class.objects