from rest_framework import serializers


class CompanyShopItemSerializer(serializers.ListSerializer):
    child = serializers.CharField()

class CompanyShopListSerializer(serializers.Serializer):
    shops = CompanyShopItemSerializer(many=False)