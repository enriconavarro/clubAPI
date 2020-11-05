from django.urls import include, path
from rest_framework import routers
from club import views

router = routers.DefaultRouter()
router.register(r'clubs', views.ClubViewSet)
router.register(r'players', views.PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
