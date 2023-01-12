from rest_framework import routers

from django.urls import path, re_path, include
from .views import BlogViewSet

router = routers.DefaultRouter(trailing_slash=False)


router.register("blog", BlogViewSet)

urlpatterns = [
    path('', include(router.urls))
]