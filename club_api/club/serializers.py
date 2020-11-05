from rest_framework import serializers

from .models import Club, Player


class ClubListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ['url', 'name', 'city']


class ClubDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class PlayerListSerializer(serializers.HyperlinkedModelSerializer):
    club = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Player
        fields = ['url', 'name', 'club']


class PlayerDetailSerializer(serializers.HyperlinkedModelSerializer):
    club = serializers.SlugRelatedField(slug_field='name', queryset=Club.objects.all())

    class Meta:
        model = Player
        fields = ['url', 'name', 'age', 'height', 'weight', 'club']