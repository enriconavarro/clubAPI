from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import League, Team, Player
from .serializers import (
    TeamListSerializer,
    TeamDetailSerializer,
    PlayerListSerializer,
    PlayerDetailSerializer,
    LeagueListSerializer,
    LeagueDetailSerializer,
    LeagueCreateUpdateSerializer,
    TeamSerializer,
    PlayerSerializer,
    LeagueSerializer
)
from config.settings import EXPORT_BUCKET_NAME, LOCAL_FILE_VAL
from utils.file_utils import write_export
from utils.s3_utils import send_export

import datetime, json


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed, created, edited or deleted.
    """
    serializers = {
        'default': TeamDetailSerializer,
        'list': TeamListSerializer
    }
    queryset = Team.objects.all().order_by("name")
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'city', 'championships_won', 'coach']

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    @action(methods=['get'], detail=True)
    def export(self, request, pk):
        date = datetime.datetime.now()
        team_string = TeamSerializer(self.get_object()).data
        team_f_name = f'team_{pk}_{date.hour}:{date.minute}:{date.second}_{date.day}_{date.month}_{date.year}.json'

        if EXPORT_BUCKET_NAME == LOCAL_FILE_VAL:
            write_export([
                [f'/tmp/{team_f_name}', json.dumps(team_string)]
            ])
            return Response(status=status.HTTP_200_OK, data=f'Successfully created {team_f_name} file in /tmp.')
        else:
            team_byte = JSONRenderer().render(teams_string)
            send_export(EXPORT_BUCKET_NAME,
            [
                [team_f_name, team_byte]
            ])
            return Response(status=status.HTTP_200_OK, data=f'Successfully send {team_f_name} to S3 bucket {EXPORT_BUCKET_NAME}.')

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed, created, edited or deleted.
    """
    serializers = {
        'default': PlayerDetailSerializer,
        'list': PlayerListSerializer
    }
    queryset = Player.objects.all().order_by("name")
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'position', 'team__name']

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    @action(methods=['get'], detail=True)
    def export(self, request, pk):
        date = datetime.datetime.now()
        player_string = PlayerSerializer(self.get_object()).data
        player_f_name = f'player_{pk}_{date.hour}:{date.minute}:{date.second}_{date.day}_{date.month}_{date.year}.json'

        if EXPORT_BUCKET_NAME == LOCAL_FILE_VAL:
            write_export([
                [f'/tmp/{player_f_name}', json.dumps(player_string)]
            ])
            return Response(status=status.HTTP_200_OK, data=f'Successfully created {player_f_name} file in /tmp.')
        else:
            player_byte = JSONRenderer().render(players_string)
            send_export(EXPORT_BUCKET_NAME,
            [
                [player_f_name, player_byte]
            ])
            return Response(status=status.HTTP_200_OK, data=f'Successfully send {player_f_name} to S3 bucket {EXPORT_BUCKET_NAME}.')

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
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country', 'teams__name', 'teams__player__name']

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    @action(methods=['get'], detail=True)
    def export(self, request, pk):
        date = datetime.datetime.now()
        league_string = LeagueSerializer(self.get_object()).data
        league_f_name = f'league_{pk}_{date.hour}:{date.minute}:{date.second}_{date.day}_{date.month}_{date.year}.json'

        if EXPORT_BUCKET_NAME == LOCAL_FILE_VAL:
            write_export([
                [f'/tmp/{league_f_name}', json.dumps(league_string)]
            ])
            return Response(status=status.HTTP_200_OK, data=f'Successfully created {league_f_name} file in /tmp.')
        else:
            league_byte = JSONRenderer().render(leagues_string)
            send_export(EXPORT_BUCKET_NAME,
            [
                [league_f_name, league_byte]
            ])
            return Response(status=status.HTTP_200_OK, data=f'Successfully send {league_f_name} to S3 bucket {EXPORT_BUCKET_NAME}.')
