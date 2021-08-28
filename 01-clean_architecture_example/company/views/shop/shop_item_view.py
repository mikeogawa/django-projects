from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.commons import viewsets
from company import serializers
from company.use_cases.shop import item as use_case


class ShopItemView(viewsets.RelationViewSet):
    """
    Shop Item View
    """
    serializer_class_dict = {
        'connect': serializers.ShopItemListSerializer,
        'disconnect': serializers.ShopItemListSerializer,
        'default': serializers.ItemListSerializer,
    }
    serializer_alias_dict = {
        'default': 'items',
    }
    use_case_dict = {
        'connect': use_case.ConnectItem,
        'disconnect': use_case.DisconnectItem,
        'default': use_case.ListItem,
    }

    # LookUp
    lookup_field = 'id'

    def list(self, request, shop_id:str, *args, **kwargs) -> Response:
        
        return super().list(request, shop_id, *args, **kwargs)

    @action(methods=['put'],suffix='connect', detail=False)
    def connect(self, request, shop_id:str, *args, **kwargs) -> Response:

        return super().connect(request, shop_id, *args, **kwargs)

    @action(methods=['put'],suffix='disconnect', detail=False)
    def disconnect(self, request, shop_id:str, *args, **kwargs) -> Response:

        return super().disconnect(request, shop_id, *args, **kwargs)