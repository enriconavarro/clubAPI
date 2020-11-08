from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist 
from .models import League, Team, Player

class LeagueListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = ['url', 'id', 'name', 'country', 'number_teams']


class TeamListSerializer(serializers.HyperlinkedModelSerializer):
    league = LeagueListSerializer(read_only=True, many=True)
    
    class Meta:
        model = Team
        fields = ['url', 'id', 'name', 'city', 'league']


class PlayerListSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamListSerializer(read_only=True, many=True)

    class Meta:
        model = Player
        fields = ['url', 'id', 'name', 'position', 'team']


class TeamDetailSerializer(serializers.HyperlinkedModelSerializer):
    league = LeagueListSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ['url', 'id', 'name', 'city', 'championships_won', 'coach', 'number_players', 'league']


class PlayerDetailSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamListSerializer(read_only=True, many=True)

    class Meta:
        model = Player
        fields = ['url', 'id', 'name', 'age', 'position', 'appearance', 'team']


class LeagueDetailSerializer(serializers.HyperlinkedModelSerializer):
    teams = TeamListSerializer(read_only=True, many=True)
    current_champion = serializers.SlugRelatedField(read_only=True, slug_field='name')
    most_championships = serializers.SlugRelatedField(read_only=True, slug_field='name')
    most_appearances = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = League
        fields = ['url', 'id', 'name', 'country', 'number_teams', 'current_champion', 'most_championships', 'most_appearances', 'teams']

class TeamNestedSerializer(serializers.ModelSerializer):
    serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    championships_won = serializers.IntegerField(required=False)
    coach = serializers.CharField(required=False)
    number_players = serializers.IntegerField(required=False)

    class Meta:
        model = Team
        fields = ['id', 'name', 'city', 'championships_won', 'coach', 'number_players']

class LeagueCreateUpdateSerializer(serializers.ModelSerializer):
    teams = TeamNestedSerializer(many=True)

    def create(self, validated_data):
        teams_data = validated_data.pop('teams')
        league = League.objects.create(**validated_data)
        teams = []

        for team_data in teams_data:
            team_id = team_data.pop('id', None)
            team, _ = Team.objects.get_or_create(id=team_id, defaults=team_data)
            teams.append(team)

        league.teams.add(*teams)
        return league

    class Meta:
        model = League
        fields = ['url', 'id', 'name', 'country', 'number_teams', 'teams']
