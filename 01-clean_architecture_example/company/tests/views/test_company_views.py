from django.test.client import Client
from rest_framework import status

from api.commons.tests import TestCase
from company.models import Company
from ..test_seeds import TestSeed

class TestCompanyView(TestCase):

    base_url = '/company/v1/'
    target_url = 'companies'

    model_class_field_list = ['name', 'code']
    exclude_model_class_field_list = ['id','created_at', 'updated_at']

    serializer_alias_dict = {
        'list': 'companies',
        'default': 'company',
    }

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.seeds = TestSeed()
        cls.seeds.setUp()

    def test_list(self):
        
        url = self.url()
        response = self.client.get(str(url))
        response_json = response.json()
        alias = self.get_serializer_alias('list')
        self.assertEqual(2,len(response_json[alias]))

        fields = self.get_model_fields()
        objs = self.seeds.companies

        for response_data in response_json[alias]:
            obj = [obj for obj in objs if str(obj.id) == response_data["id"]][0]
            self.check_fields_value(obj, response_data, fields)
            

    def test_retreive(self):
        
        obj = self.seeds.companies[0]
        url = self.url(str(obj.id))
        response = self.client.get(url)
        response_json = response.json()
        alias = self.get_serializer_alias()
        fields = self.get_model_fields()

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.check_fields_value(obj, response_json[alias], fields)

    def test_create(self):

        obj = Company(
            name = 'x',
            code = 'x',
        )
        url = self.url()
        obj_dict = {k:v for k,v in obj.to_dict().items() if k not in self.exclude_model_class_field_list}
        alias = self.get_serializer_alias()
        response = self.client.post(url, data={alias:obj_dict}, content_type='application/json')
        response_json = response.json()
        fields = self.get_model_fields(exclude=['id'])

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        self.check_fields_value(obj, response_json[alias], fields)

    def test_update(self):

        obj = self.seeds.companies[0]
        obj.name = 'y'
        url = self.url(str(obj.id))
        alias = self.get_serializer_alias()
        obj_dict = {k:v for k,v in obj.to_dict().items() if k not in self.exclude_model_class_field_list}
        response = self.client.put(url, data={alias:obj_dict}, content_type='application/json')
        response_json = response.json()
        
        fields = self.get_model_fields(exclude=['id'])

        self.check_fields_value(obj, response_json[alias], fields)

    def test_delete(self):

        obj = self.seeds.companies[0]
        url = self.url(str(obj.id))
        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    # TODO: ....