from typing import Dict
from company.repositories import CompanyRepository
from api.commons import exceptions
from api.commons import BaseUseCase

class CreateCompany(BaseUseCase):

    def __init__(self):

        self.repository = CompanyRepository()

    def execute(self, data: Dict[str, str]):

        obj = self.repository.get_by_code(data["code"])

        if obj:
            raise exceptions.ConflictError({'code': 'Conflict'})

        obj = self.repository.create(data)
        
        return obj
