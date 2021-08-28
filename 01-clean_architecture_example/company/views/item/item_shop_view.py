from rest_framework.response import Response

from api.commons import viewsets
from company import serializers
from company.use_cases.item import shop as use_case


class ItemShopView(viewsets.RelationViewSet):
    """
    Item Shop View
    """
    serializer_class_dict = {
        'default': serializers.ShopListSerializer,
    }
    serializer_alias_dict = {
        'default': 'shops',
    }
    use_case_dict = {
        'default': use_case.ListShop,
    }

    # LookUp
    lookup_field = 'id'

    def list(self, request, item_id:str, *args, **kwargs) -> Response:

        return super().list(request, item_id, *args, **kwargs)
