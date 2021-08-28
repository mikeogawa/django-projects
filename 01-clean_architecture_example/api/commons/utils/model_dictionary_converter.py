from django.db import models
from django.db.models.fields.related import ManyToManyField

class ModelDictonaryConverter:
    """
    Django Model => Dictionary Converter
    """

    def __init__(self, obj):
        self.obj = obj
        self.data = {}

    def _set_many_to_many(self, field):
        obj = self.obj

        if obj.id is None:
            self.data[field.name] = []
        else:
            self.data[field.name] = list(field.value_from_object(obj).values_list('id', flat=True))

    def _set_date(self, field):
        obj = self.obj

        if field.value_from_object(obj) is not None:
            self.data[field.name] = field.value_from_object(obj).timestamp()
        else:
            self.data[field.name] = None

    def _set_value(self, field):
        obj = self.obj

        self.data[field.name] = field.value_from_object(obj)

    def execute(self):
        opts = self.obj._meta

        for field in opts.concrete_fields + opts.many_to_many:

            if isinstance(field, ManyToManyField):
                self._set_many_to_many(field)
            elif isinstance(field, models.DateTimeField):
                self._set_date(field)
            else:
                self._set_value(field)

        return self.data
