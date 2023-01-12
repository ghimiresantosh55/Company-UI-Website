from rest_framework import routers

from django.urls import path, re_path, include
from .views import GalleryViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register("gallery", GalleryViewSet)

urlpatterns = [
    path('', include(router.urls))
]