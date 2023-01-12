from rest_framework import routers

from django.urls import path, re_path, include
from .views import SolutionViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register("solution", SolutionViewSet)

urlpatterns = [
    path('', include(router.urls))
]