from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
        
    class Meta:
        
        model = Account
        fields = ['id','email','password', 'first_name', 'last_name', 'is_seller', 'data_joined']
        read_only_fields =  ['data_joined']
        extra_kwargs = {"password": {"write_only": True}}
    
    def validate_email(self, value):
        if Account.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("email already exists")
        return value
    
    def create(self, validated_data):

        return Account.objects.create_user(**validated_data)
        
     
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
