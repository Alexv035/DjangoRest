from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.routers import DefaultRouter

from authors.views import AuthorModelViewSet
from todo import views
from todo.models import Project
from todo.serializers import ProjectSerializer
from todo.views import AuthorViewSet, BookViewSet, ProjectModelViewSet

router = DefaultRouter()
router.register("authors", AuthorModelViewSet)
router.register("project", ProjectModelViewSet)
router.register("base", views.ProjectViewSet, basename="project")

filter_router = DefaultRouter()
filter_router.register("param", views.ProjectParamFilterViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

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
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    path("api-token-auth/", views.obtain_auth_token),

]


class ProjectDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
