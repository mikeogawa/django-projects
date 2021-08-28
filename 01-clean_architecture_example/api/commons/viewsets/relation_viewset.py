from rest_framework.decorators import action
from rest_framework.response import Response

from .base_viewset import BaseViewSet

class RelationViewSet(BaseViewSet):
    """
    Relation ViewSet
    """

    # LookUp
    lookup_field = 'id'

    def list(self, request, id_:str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        objs = case.execute(id_)

        serializer = self.get_serializer({alias: objs})
        return Response(serializer.data)

    def connect(self, request, id_:str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        objs = case.execute(id_, serializer.validated_data[alias])

        serializer = self.get_serializer({alias: objs})
        return Response(serializer.data)

    def disconnect(self, request, id_:str, *args, **kwargs) -> Response:
        alias = self.get_serializer_alias()
        case = self.get_use_case()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        objs = case.execute(id_, serializer.validated_data[alias])

        serializer = self.get_serializer({alias: objs})
        return Response(serializer.data)
