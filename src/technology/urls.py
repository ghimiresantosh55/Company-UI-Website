from rest_framework import routers

from django.urls import path, re_path, include
from .views import TechnologyViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register("technology", TechnologyViewSet)

urlpatterns = [
    path('', include(router.urls))
]