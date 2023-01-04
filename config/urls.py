from django.contrib import admin
from django.urls import include, path
<<<<<<< HEAD
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
=======
from graphene_django.views import GraphQLView
>>>>>>> 9ba6b6cecab3e676baa2361d4518f85120416a5d
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from authors.views import AuthorModelViewSet
from todo import views
from todo.models import Project
from todo.serializers import ProjectSerializer
<<<<<<< HEAD
from todo.views import ProjectModelViewSet
from userapp.views import UserListAPIView
=======
from todo.views import AuthorViewSet, BookViewSet, ProjectModelViewSet
>>>>>>> 9ba6b6cecab3e676baa2361d4518f85120416a5d

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
<<<<<<< HEAD
    path(r"^api/(?P<version>\d\.\d)/users/$", UserListAPIView.as_view()),
    path("api/users/0.1", include("userapp.urls", namespace="0.1")),
    path("api/users/0.2", include("userapp.urls", namespace="0.2")),
    path(r"^swagger(?P<format>\.json|\.yaml)$", get_schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", get_schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", get_schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
=======
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    path("api-token-auth/", views.obtain_auth_token),

>>>>>>> 9ba6b6cecab3e676baa2361d4518f85120416a5d
]


class ProjectDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version="0.1",
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)
