from django.shortcuts import get_object_or_404, render
from rest_framework import mixins, viewsets
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.


class ProjectModelViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectAPIVIew(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        articles = Project.objects.all()
        serializer = ProjectSerializer(articles, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def project_view(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


class ArticleCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    @action(detail=True, methods=["get"])
    def project_text_only(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        return Response({"project.text": project.text})

    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class ProjectCustomViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class ProjectQuerysetFilterViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()

    def get_queryset(self):
        return Project.objects.filter(name__contains="python")


class ProjectKwargsFilterView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Project.objects.filter(name__contains=name)


class ProjectParamFilterViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        name = self.request.query_params.get("name", "")
        projects = Project.objects.all()
        if name:
            projects = projects.filter(name__contains=name)
        return projects


class ProjectDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = ["notes", "user"]


class ProjectCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ProjectLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
