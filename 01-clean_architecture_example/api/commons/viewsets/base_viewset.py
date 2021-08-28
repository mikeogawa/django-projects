from typing import Dict, List, Optional, Tuple, Type

from rest_framework import serializers, viewsets
from rest_framework.permissions import BasePermission

from api.commons import BaseUseCase


class BaseViewSet(viewsets.GenericViewSet):
    """
    ViewSet
    """
    class Meta:
        abstract = True

    # Permissions
    permission_classes_dict: Dict[str, Tuple] = {}

    # Serializer
    serializer_class_dict: Dict[str, serializers.Serializer] = {}
    serializer_alias_dict: Dict[str, str] = {}

    # UseCase
    use_case_dict: Dict[str, Type[BaseUseCase]] = {}

    # LookUp
    lookup_field = 'id'

    def get_permissions(self) -> List[BasePermission]:
        permission_classes = (
            self.permission_classes_dict.get(self.action) or
            self.permission_classes_dict.get('default') or
            self.permission_classes
        )
        return [permission() for permission in permission_classes]

    def get_serializer_class(self) -> serializers.Serializer:
        return (
            self.serializer_class_dict.get(self.action) or
            self.serializer_class_dict.get('default') or
            self.serializer_class_dict['list']
        )

    def get_serializer_alias(self) -> Optional[str]:
        return (
            self.serializer_alias_dict.get(self.action) or
            self.serializer_alias_dict.get('default') or
            self.serializer_alias_dict['list']
        )

    def get_use_case(self, *args, **kwargs) -> BaseUseCase:
        func = (
            self.use_case_dict.get(self.action) or
            self.use_case_dict.get('default') or
            self.use_case_dict['list']
        )
        return func(*args, **kwargs)

