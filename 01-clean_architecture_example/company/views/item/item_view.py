from rest_framework import status
from rest_framework.response import Response

from api.commons import viewsets
from company import serializers
from company.use_cases import item as use_case


class ItemView(viewsets.SingleViewSet):
    """
    Item View
    """
    serializer_class_dict = {
        'list': serializers.ItemListSerializer,
        'default': serializers.ItemItemSerializer,
    }
    serializer_alias_dict = {
        'list': 'items',
        'default': 'item',
    }
    use_case_dict = {
        'list': use_case.ListItem,
        'create': use_case.CreateItem,
        'retrieve': use_case.GetItem,
        'update': use_case.UpdateItem,
        'destroy': use_case.DeleteItem,
    }

    # LookUp
    lookup_field = 'id'

