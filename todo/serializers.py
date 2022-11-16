from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Project, TODO


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    # notes = serializers.CharField(max_length=64)
    # date_creation = serializers.DateField()
    # date_update = serializers.DateField()
    # user = serializers.CharField(max_length=64)
    # actives = serializers.BooleanField()
