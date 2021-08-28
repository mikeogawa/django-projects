from rest_framework import serializers


class ShopItemItemSerializer(serializers.ListSerializer):
    child = serializers.CharField()

class ShopItemListSerializer(serializers.Serializer):
    items = ShopItemItemSerializer(many=False)