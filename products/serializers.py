from accounts.serializers import AccountSerializer
from rest_framework import serializers

from .models import Product

class CreateProductSerializer(serializers.ModelSerializer):
    seller = AccountSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ['id', 'is_active']
        
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
        
class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['description', 'price', 'quantity', 'is_active', 'seller_id']  
        read_only_fields = ['description', 'price', 'quantity', 'is_active', 'seller_id']  
        
        