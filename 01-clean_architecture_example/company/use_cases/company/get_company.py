from typing import Dict
from company.repositories import CompanyRepository
from api.commons import exceptions
from api.commons import BaseUseCase

class GetCompany(BaseUseCase):

    def __init__(self):

        self.repository = CompanyRepository()

    def execute(self, id: str):

        obj = self.repository.get_by_id(id)

        if obj is None:
            raise exceptions.NotFound({'id': 'Not found'})

        return obj
