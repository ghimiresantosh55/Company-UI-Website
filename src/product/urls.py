from rest_framework import routers

from django.urls import path, re_path, include
from .views import ProductViewSet

router = routers.DefaultRouter(trailing_slash=False)


router.register("product", ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]