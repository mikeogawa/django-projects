
from django.test import TestCase
from company.models import Company
from company.repositories import (
    CompanyRepository
)
from ..test_seeds import TestSeed



class TestCompanyRepository(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.repository = CompanyRepository()
        cls.seeds = TestSeed()
        cls.seeds.setUp()

    def test_all(self):

        objs = list(self.repository.list())
        self.assertEqual(2,len(objs))

    def test_get_by_id(self):
        
        target_obj = self.seeds.companies[0]
        obj = self.repository.get_by_id(target_obj.id)

        self.assertTrue(isinstance(target_obj, Company))
        self.assertEqual(target_obj.id, str(obj.id))
        self.assertEqual(target_obj.name, obj.name)
        self.assertEqual(target_obj.code, obj.code)

    def test_get_by_name(self):
        
        target_obj = self.seeds.companies[0]
        obj = self.repository.get_by_name(target_obj.name)

        self.assertTrue(isinstance(target_obj, Company))
        self.assertEqual(target_obj.id, str(obj.id))
        self.assertEqual(target_obj.name, obj.name)
        self.assertEqual(target_obj.code, obj.code)

    def test_get_by_code(self):
        
        target_obj = self.seeds.companies[0]
        obj = self.repository.get_by_code(target_obj.code)

        self.assertTrue(isinstance(target_obj, Company))
        self.assertEqual(target_obj.id, str(obj.id))
        self.assertEqual(target_obj.name, obj.name)
        self.assertEqual(target_obj.code, obj.code)

    # TODO: ....