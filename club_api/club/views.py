from rest_framework import viewsets
from .models import Club, Player
from .serializers import (
    ClubListSerializer,
    ClubDetailSerializer,
    PlayerListSerializer,
    PlayerDetailSerializer
)


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