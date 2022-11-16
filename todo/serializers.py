from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Project, TODO


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class AuthorSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()
    author = Author('Грин', 1880)
    serializer = AuthorSerializer(author)
    print(serializer.data)  # {'name': 'Грин', 'birthday_year': 1880}
    print(type(serializer.data))
    #
    'rest_framework.utils.serializer_helpers.ReturnDict' >
    renderer = JSONRenderer()
    json_bytes = renderer.render(serializer.data)
    print(json_bytes)
    b'{"name":"\xd0\x93\xd1\x80\xd0\xb8\xd0\xbd","birthday_year":1880}'
    print(type(json_bytes))  # <class 'bytes'>
    <class
    #
    stream = io.BytesIO(json_bytes)
    data = JSONParser().parse(stream)
    print(data)  # {'name': 'Грин', 'birthday_year': 1880}
    print(type(data))  # <class 'dict'>
