from company.models import (
    Company,
    Shop,
    Item,
)


class TestSeed:

    def setUp(self):
        companies = [
            Company(
                id='d3ff4778-8e3c-45db-8727-617245c6688d', code='CA0001',
                name='company_A',
                ),
            Company(
                id='b10d9183-a57c-4c92-9f14-623e889b7fc3',
                code='CB0001',
                name='company_B',
                ),
        ]

        Company.objects.bulk_create(companies)

        shops = [
            Shop(
                id='4bab67be-d852-4ca5-801c-d4e8ae7820be',
                code='SA0001',
                name='shop_A1',
                company=companies[0],
                ),
            Shop(
                id='830b10f9-df52-40ce-acaa-6878cb60db45',
                code='SA0002',
                name='shop_A2',
                company=companies[0],
                ),
            Shop(
                id='47311d5b-6314-4ca5-af0e-0d14bda75c7f',
                code='SA0003',
                name='shop_A3',
                company=companies[0],
                ),
            Shop(
                id='91a01c1b-dffe-4318-96df-c8b464c71e0b',
                code='SB0001',
                name='shop_B1',
                company=companies[1],
                ),
        ]
        Shop.objects.bulk_create(shops)

        items = [
            Item(
                id='0fa5b590-7424-445e-a5b0-10276de037b4',code='IA0001',
                name='item_01',
                ),
            Item(
                id='a75120a3-91cb-4e2e-b42f-91af56707779',
                code='IA0002',
                name='item_02',
                ),
            Item(
                id='74b034b9-7021-440a-9ccc-88067499f27a',code='IA0004',
                name='item_04',
                ),
            Item(
                id='661e0988-d0d4-4a76-affa-51823d050fdc',
                code='IA0003',
                name='item_03',
                ),
        ]

        # Entity
        Item.objects.bulk_create(items)
        for shop in shops[:2]:
            shop.items.add(*items[:2])
        for shop in shops[2:]:
            shop.items.add(*items[2:])

        self.companies = companies
        self.shops = shops
        self.items = items


