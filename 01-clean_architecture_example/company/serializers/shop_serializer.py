from rest_framework import serializers

class ShopSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    code = serializers.CharField()
    name = serializers.CharField()

class ShopListSerializer(serializers.Serializer):
    shops = ShopSerializer(many=True)

class ShopItemSerializer(serializers.Serializer):
    shop = ShopSerializer(many=False)
