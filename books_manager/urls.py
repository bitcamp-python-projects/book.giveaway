from django.urls import path
from .views import index, UserRegistrationView, UserLoginView

urlpatterns = [
    path('', index),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]