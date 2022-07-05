from django.urls import path
from . import views


urlpatterns = [
    path("accounts/", views.ListCreateAccountView.as_view()),
    path("accounts/newest/<int:num>/", views.ListAccountView.as_view()),
    path("login/", views.LoginView.as_view())
]