from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    code = serializers.CharField()
    name = serializers.CharField()

class ItemListSerializer(serializers.Serializer):
    items = ItemSerializer(many=True)

class ItemItemSerializer(serializers.Serializer):
    item = ItemSerializer(many=False)
