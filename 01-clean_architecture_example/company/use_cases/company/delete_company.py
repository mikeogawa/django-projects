from typing import Dict
from company.repositories import CompanyRepository
from api.commons import (
    BaseUseCase,
)

class DeleteCompany(BaseUseCase):

    def __init__(self):

        self.repository = CompanyRepository()

    def execute(self, id: str):

        obj = self.repository.get_by_id(id)

        if obj:
            obj.delete()

