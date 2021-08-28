import uuid

from django.db import models
from django.db.models.fields.related import ManyToManyField

from .utils import ModelDictonaryConverter

class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def to_dict(self):
        model_dictionary_creator = ModelDictonaryConverter(self)
        return model_dictionary_creator.execute()
