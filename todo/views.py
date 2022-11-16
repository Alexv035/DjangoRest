from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Project, TODO
from .serializers import ProjectModelSerializer

# Create your views here.


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
