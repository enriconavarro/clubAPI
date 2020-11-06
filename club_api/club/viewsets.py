from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Club, Player
from .serializers import (
    ClubListSerializer,
    ClubDetailSerializer,
    PlayerListSerializer,
    PlayerDetailSerializer
)
from club_api.settings import BACKUP_BUCKET_NAME, DB_FILE_PATH
import boto3
import datetime


class ClubViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clubs to be viewed, created, edited or deleted.
    """
    serializers = {
        'default': ClubDetailSerializer,
        'list': ClubListSerializer
    }
    queryset = Club.objects.all()
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
    queryset = Player.objects.all()
    filter_fields = ('name', 'club')

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
        if BACKUP_BUCKET_NAME == 'LOCAL':
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Running locally, can`t send the backup to s3 ;)')

        client = boto3.client('s3')
        name = f'backup_{datetime.datetime.now()}.backup.sqlite3'
        
        data = None
        with open(DB_FILE_PATH, "rb") as bfile:
            data = bytearray(bfile.read())

        client.put_object(Bucket=BACKUP_BUCKET_NAME, Key=name, Body=data)
        return Response(status=status.HTTP_200_OK, data=f'Successfully send the backup {name} to S3.')
