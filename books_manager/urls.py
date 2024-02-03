from django.urls import path
from .views import *
from .views import RegisterUserView, CustomAuthToken

urlpatterns = [
    path('', index),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]