from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect  # Added for redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="WorkBE API",
        default_version='v1',
        description="API documentation for WorkBE",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@workbe.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def redirect_to_swagger(request):
    return HttpResponseRedirect('/swagger/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('users.urls')),
    # Swagger/OpenAPI URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', 
            schema_view.without_ui(cache_timeout=0), 
            name='schema-json'),
    re_path(r'^swagger/$', 
            schema_view.with_ui('swagger', cache_timeout=0), 
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', 
            schema_view.with_ui('redoc', cache_timeout=0), 
            name='schema-redoc'),
    path('', redirect_to_swagger, name='home'),  # Added root redirect
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
