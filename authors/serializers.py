from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

from .models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)
