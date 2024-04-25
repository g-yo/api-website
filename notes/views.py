from django.shortcuts import render
from .models import Movies
from rest_framework import generics

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

from rest_framework import viewsets
from .serializers import Userserializer,MovieSerializer

# Create your views here.

#notes manageent view
class MoviesViewset(generics.ListCreateAPIView):
    serializer_class=MovieSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Movies.objects.filter(user=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)


#delte a file
            
class MovieDelete(generics.DestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Movies.objects.filter(user=user)


#usser creation view 
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]


