from django.urls import path

from .views import ListCreateProductView, ListUpdateProductView

urlpatterns = [
    path("products/", ListCreateProductView.as_view()),
    path("products/<pk>/", ListUpdateProductView.as_view()),
]
