from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from core import viewsets

router = routers.DefaultRouter()
router.register(r'leagues', viewsets.LeagueViewSet)
router.register(r'teams', viewsets.TeamViewSet)
router.register(r'players', viewsets.PlayerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('openapi', get_schema_view(
        title="leagueAPI",
        description="API for football leagues!",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
