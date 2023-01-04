from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorModelSerializer, AuthorSerializer, AuthorSerializerBase

# Create your views here.


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.version == "2.0":
            return AuthorSerializerBase
        return AuthorSerializer
