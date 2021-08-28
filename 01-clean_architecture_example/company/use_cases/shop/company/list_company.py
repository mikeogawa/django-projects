from typing import Dict
from company.repositories import CompanyRepository
from api.commons import BaseUseCase

class ListCompany(BaseUseCase):

    def __init__(self):

        self.repository = CompanyRepository()

    def execute(self, id_: str):

        return self.repository.filter_eq_shop_id(id_)
