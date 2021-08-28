from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework_nested import routers as routers_nested

from .views import (
    CompanyView,
    CompanyShopView,
    ItemView,
    ItemShopView,
    ShopView,
    ShopCompanyView,
    ShopItemView,
)

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'companies', CompanyView, basename='company')
router.register(r'shops', ShopView, basename='shop')
router.register(r'items', ItemView, basename='item')

# companies/{}/shop
company_router = routers_nested.NestedSimpleRouter(router, r'companies', lookup='company', trailing_slash=False)
company_router.register(r'shops', CompanyShopView, basename='compnay-shop')

# shops/{}/companies, shops/{}/items
shop_router = routers_nested.NestedSimpleRouter(router, r'shops', lookup='shop', trailing_slash=False)
shop_router.register(r'items', ShopItemView, basename='shop-compnay')
shop_router.register(r'companies', ShopCompanyView, basename='shop-item')

# items/{}/shop
item_router = routers_nested.NestedSimpleRouter(router, r'items', lookup='item', trailing_slash=False)
item_router.register(r'shops', ItemShopView, basename='shop-item')


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'', include(company_router.urls)),
    url(r'', include(shop_router.urls)),
    url(r'', include(item_router.urls)),
]
