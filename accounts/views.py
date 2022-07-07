from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from accounts.serializers import AccountSerializer, LoginSerializer


class ListCreateAccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )        
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({"token": token.key}) 
            
        return Response(
            {"detail": "invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED
        )

class ListAccountView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer()
    
    def get_queryset(self):
        num_accounts = self.kwargs["num"]
        return self.queryset.order_by("-data_joined")[0:num_accounts] 