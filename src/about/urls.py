from rest_framework import routers

from django.urls import path, re_path, include
from .views import OurTeamViewSet, CeoMessageViewSet
router = routers.DefaultRouter(trailing_slash=False)


router.register("our-team", OurTeamViewSet)
router.register("ceo-message",CeoMessageViewSet)  


urlpatterns = [
    path('', include(router.urls))
]