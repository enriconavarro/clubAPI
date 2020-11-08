from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from core import viewsets

router = routers.DefaultRouter()
router.register(r'leagues', viewsets.LeagueViewSet)
router.register(r'teams', viewsets.TeamViewSet)
router.register(r'players', viewsets.PlayerViewSet)
router.register('backup', viewsets.BackupViewSet, basename='backup')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
