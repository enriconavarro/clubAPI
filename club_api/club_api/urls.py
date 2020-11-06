from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from club import viewsets

router = routers.DefaultRouter()
router.register(r'clubs', viewsets.ClubViewSet)
router.register(r'players', viewsets.PlayerViewSet)
router.register('backup', viewsets.BackupViewSet, basename='backup')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
