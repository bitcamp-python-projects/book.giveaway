from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('<h1>This is Simply A Test That EveryThing Is Working!</h1>')


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        
        username = serializer.validated_data['email'].split('@')[0]
        serializer.save(username=username)
        user = serializer.instance
        Token.objects.create(user=user)


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email'] 
        user = CustomUser.objects.get(email=email) 
        Token.objects.get_or_create(user=user)
        return Response({'token': user.auth_token.key}, status=status.HTTP_200_OK)