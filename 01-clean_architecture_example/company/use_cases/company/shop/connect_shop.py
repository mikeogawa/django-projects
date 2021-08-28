from typing import List
from company.repositories.company import CompanyRepository
from api.commons import exceptions
from api.commons import BaseUseCase
from company.repositories import (
    CompanyRepository,
    ShopRepository,
)


class ConnectShop(BaseUseCase):

    def __init__(self):

        self.company_repository = CompanyRepository()
        self.shop_repository = ShopRepository()

    def execute(self, company_id: str, shop_ids: List[str]):

        company = self.company_repository.get_by_id(company_id)

        if company is None:
            raise exceptions.NotFound()

        shops = self.shop_repository.filter_in_id_list(shop_ids)

        self.shop_repository.bulk_update_shop_id_to_company(shops, company)

        return [str(s.id) for s in shops]
