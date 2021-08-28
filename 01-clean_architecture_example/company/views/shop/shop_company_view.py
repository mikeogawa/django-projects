from rest_framework.response import Response

from api.commons import viewsets
from company import serializers
from company.use_cases.shop import company as use_case


class ShopCompanyView(viewsets.RelationViewSet):
    """
    Shop Company View
    """
    serializer_class_dict = {
        'default': serializers.CompanyListSerializer,
    }
    serializer_alias_dict = {
        'default': 'companies',
    }
    use_case_dict = {
        'default': use_case.ListCompany,
    }

    # LookUp
    lookup_field = 'id'

    def list(self, request, shop_id:str, *args, **kwargs) -> Response:

        return super().list(request, shop_id, *args, **kwargs)
