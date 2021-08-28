from typing import Dict
from company.repositories import CompanyRepository
from api.commons import BaseUseCase

class ListCompany(BaseUseCase):

    def __init__(self):

        self.repository = CompanyRepository()

    def execute(self):

        return self.repository.list()
