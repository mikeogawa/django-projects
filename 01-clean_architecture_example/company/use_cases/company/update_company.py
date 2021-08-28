from typing import Dict
from company.repositories import CompanyRepository
from api.commons import exceptions
from api.commons import BaseUseCase

class UpdateCompany(BaseUseCase):

    def __init__(self):

        self.repository = CompanyRepository()

    def execute(self, id:str, data: Dict[str, str]):

        obj = self.repository.get_by_id(id)

        if obj is None:
            raise exceptions.NotFound({'id': 'Not found'})

        self.repository.update(obj, data)
        
        return obj
