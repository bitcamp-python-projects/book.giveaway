from django.urls import path
from .views import *
from .views import RegisterUserView, CustomAuthToken, BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('', index),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]