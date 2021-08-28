from rest_framework import serializers

class CompanySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    code = serializers.CharField()
    name = serializers.CharField()


class CompanyListSerializer(serializers.Serializer):
    companies = CompanySerializer(many=True)

class CompanyItemSerializer(serializers.Serializer):
    company = CompanySerializer(many=False)
