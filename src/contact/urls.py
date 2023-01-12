from rest_framework import routers

from django.urls import path, re_path, include
from .views import ContactViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register("contact", ContactViewSet)

urlpatterns = [
    path('', include(router.urls))
]