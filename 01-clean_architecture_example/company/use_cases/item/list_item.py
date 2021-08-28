from typing import Dict
from company.repositories import ItemRepository
from api.commons import BaseUseCase

class ListItem(BaseUseCase):

    def __init__(self):

        self.repository = ItemRepository()

    def execute(self):

        return self.repository.list()
