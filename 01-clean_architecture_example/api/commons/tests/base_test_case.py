import os
from typing import Dict, List, Optional

from django.db import models

from django.test.testcases import TestCase as BaseTestCase

class TestCase(BaseTestCase):
    
    # Url
    base_url: str
    target_url: str

    # model_class
    model_class_field_list: List[str]
    exclude_model_class_field_list: List[str]
    
    # Serializer
    serializer_alias_dict: Dict[str, str] = {}

    def get_serializer_alias(self, key='') -> Optional[str]:

        return self.serializer_alias_dict.get(key) or self.serializer_alias_dict['default']

    def get_model_fields(self, include: List[str] = None, exclude: List[str] = None):
        include = include or []
        exclude = exclude or []
        return [v for v in [*include, *self.model_class_field_list] if v not in exclude]

    def url(self, *args):
        return os.path.join(self.base_url, self.target_url, *args)

    def check_fields_value(self, obj: models.Model, data:Dict[str,str], fields:List[str]):
        for f in fields:
            value = str(getattr(obj, f))
            target_value = data.get(f)
            self.assertEqual(value, target_value)