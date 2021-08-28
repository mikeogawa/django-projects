from rest_framework import status
from rest_framework.response import Response

from api.commons import viewsets
from company import serializers
from company.use_cases import company as use_case


class CompanyView(viewsets.SingleViewSet):
    """
    Company View
    """
    serializer_class_dict = {
        'list': serializers.CompanyListSerializer,
        'default': serializers.CompanyItemSerializer,
    }
    serializer_alias_dict = {
        'list': 'companies',
        'default': 'company',
    }
    use_case_dict = {
        'list': use_case.ListCompany,
        'create': use_case.CreateCompany,
        'retrieve': use_case.GetCompany,
        'update': use_case.UpdateCompany,
        'destroy': use_case.GetCompany,
    }

    # LookUp
    lookup_field = 'id'
