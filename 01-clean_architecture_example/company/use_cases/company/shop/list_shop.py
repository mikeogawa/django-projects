from api.commons import BaseUseCase
from company.repositories import ShopRepository


class ListShop(BaseUseCase):

    def __init__(self):

        self.repository = ShopRepository()

    def execute(self, id_: str):

        return self.repository.filter_eq_company_id(id_)
