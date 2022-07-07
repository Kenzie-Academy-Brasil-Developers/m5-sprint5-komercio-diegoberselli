from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .mixins import SerializerByMethodMixin
from .models import Product
from .serializers import CreateProductSerializer, ListProductSerializer


class ListCreateProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Product.objects.all()
    serializer_map = {
        "GET": ListProductSerializer, 
        "POST": CreateProductSerializer,
        }
    
    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)

        
class ListUpdateProductView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    
    queryset = Product.objects.all()
    serializer_map = {
        "PATCH": CreateProductSerializer, 
        "GET": ListProductSerializer,
    }
