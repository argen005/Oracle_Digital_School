from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="School API",
        default_version='v1',
        description="SCHOOL",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="argen.kubatbekov@gmail.com"),
        license=openapi.License(name="BSD License"),
        dochost="http://127.0.0.1:8000",
        schemes=['http', 'https'],
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]