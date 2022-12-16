"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.routers import DefaultRouter

from authors.views import AuthorModelViewSet
from todo import views
from todo.models import Project
from todo.serializers import ProjectSerializer
from todo.views import ProjectModelViewSet

router = DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register("project", ProjectModelViewSet)
router.register("base", views.ProjectViewSet, basename="project")

filter_router = DefaultRouter()
filter_router.register("param", views.ProjectParamFilterViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("project/", include(router.urls)),
    path("views/api-view/", views.ProjectAPIVIew.as_view()),
    path("generic/retrieve/<int:pk>/", views.ProjectRetrieveAPIView.as_view()),
    path("viewsets/", include(router.urls)),
    path("filters/kwargs/<str:name>/", views.ProjectKwargsFilterView.as_view()),
    path("filters/", include(filter_router.urls)),
]


class ProjectDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
