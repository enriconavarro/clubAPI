from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import League, Team, Player
from .serializers import (
    TeamListSerializer,
    TeamDetailSerializer,
    PlayerListSerializer,
    PlayerDetailSerializer,
    LeagueListSerializer,
    LeagueDetailSerializer,
    LeagueCreateUpdateSerializer
)
from config.settings import BACKUP_BUCKET_NAME
import boto3
import datetime


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed, created, edited or deleted.
    """
    serializers = {
        'default': TeamDetailSerializer,
        'list': TeamListSerializer
    }
    queryset = Team.objects.all().order_by("name")
    filter_fields = ('name', 'city')

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed, created, edited or deleted.
    """
    serializers = {
        'default': PlayerDetailSerializer,
        'list': PlayerListSerializer
    }
    queryset = Player.objects.all().order_by("name")
    filter_fields = ('name', 'team')

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

class LeagueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows leagues to be viewed, created, edited or deleted.
    """
    serializers = {
        'default': LeagueDetailSerializer,
        'list': LeagueListSerializer,
        'create': LeagueCreateUpdateSerializer,
        'update': LeagueCreateUpdateSerializer
    }
    queryset = League.objects.all().order_by("name")

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

class BackupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that makes a db backup and sends to S3.
    """

    pagination_class = None
    def get_queryset(self):
        return None

    def list(self, request):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED, data='WIP ;)')
