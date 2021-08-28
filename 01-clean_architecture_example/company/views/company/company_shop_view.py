from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.commons import viewsets
from company import serializers
from company.use_cases.company import shop as use_case


class CompanyShopView(viewsets.RelationViewSet):
    """
    Company Shop View
    """
    serializer_class_dict = {
        'connect': serializers.CompanyShopListSerializer,
        'disconnect': serializers.CompanyShopListSerializer,
        'list': serializers.ShopListSerializer,
    }
    serializer_alias_dict = {
        'default': 'shops',
    }
    use_case_dict = {
        'connect': use_case.ConnectShop,
        'list': use_case.ListShop,
    }

    # LookUp
    lookup_field = 'id'

    def list(self, request, company_id:str, *args, **kwargs) -> Response:
        
        return super().list(request, company_id, *args, **kwargs)

    @action(methods=['put'],suffix='connect', detail=False)
    def connect(self, request, company_id:str, *args, **kwargs) -> Response:

        return super().connect(request, company_id, *args, **kwargs)