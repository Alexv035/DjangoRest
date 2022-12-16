from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Author, Book, Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    # notes = serializers.CharField(max_length=64)
    # date_creation = serializers.DateField()
    # date_update = serializers.DateField()
    # user = serializers.CharField(max_length=64)
    # actives = serializers.BooleanField()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
