"""soori_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from soori_website import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Soori website  System",
        default_version='v1',
        description="Test",
        terms_of_service="",
        contact=openapi.Contact(email="santoshhghimire506@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('user-app/', include('src.user.urls')),
    path('core-app/', include('src.core_app.urls')),
    path('group-app/', include('src.user_group.urls')),
    path('about-us-app/', include('src.about.urls')),
    path('blog-app/' ,include('src.blog.urls')),
    path('contact-app/' ,include('src.contact.urls')),
    path('gallery-app/' ,include('src.gallery.urls')),
    path('product-app/' ,include('src.product.urls')),
    path('solution-app/' ,include('src.solution.urls')),
    path('technology-app/' ,include('src.technology.urls')),
]
