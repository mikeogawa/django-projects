from .base_viewset import BaseViewSet
from .relation_viewset import *
from .single_viewset import *


from rest_framework import status
from rest_framework.response import Response

from .base_viewset import BaseViewSet


class SingleViewSet(BaseViewSet):
    """
    Single ViewSet
    """

    # LookUp
    lookup_field = 'id'

    def list(self, request, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        objs = case.execute()

        serializer = self.get_serializer({alias: objs})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = case.execute(serializer.validated_data[alias])

        serializer = self.get_serializer({alias: obj})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, id:str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        obj = case.execute(id)

        serializer = self.get_serializer({alias: obj})
        return Response(serializer.data)

    def update(self, request, id: str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tenant = case.execute(id, serializer.validated_data[alias])

        serializer = self.get_serializer({alias: tenant})
        return Response(serializer.data)

    def destroy(self, request, id: str, *args, **kwargs) -> Response:
        case = self.get_use_case()

        case.execute(id)

        return Response(status=status.HTTP_204_NO_CONTENT)