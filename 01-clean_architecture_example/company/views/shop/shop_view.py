from rest_framework import status
from rest_framework.response import Response

from api.commons import viewsets

from company import serializers
from company.use_cases import shop as use_case


class ShopView(viewsets.SingleViewSet):
    """
    Shop View
    """
    serializer_class_dict = {
        'list': serializers.ShopListSerializer,
        'default': serializers.ShopItemSerializer,
    }
    serializer_alias_dict = {
        'list': 'shops',
        'default': 'shop',
    }
    use_case_dict = {
        'list': use_case.ListShop,
        'create': use_case.CreateShop,
        'retrieve': use_case.GetShop,
        'update': use_case.UpdateShop,
        'destroy': use_case.DeleteShop,
    }

    # LookUp
    lookup_field = 'id'
