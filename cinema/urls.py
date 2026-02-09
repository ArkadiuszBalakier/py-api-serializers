from django.urls import path, include
from rest_framework import routers

from cinema.views import ActorViewSet, GenreViewSet

app_name = 'cinema'

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r"actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
