from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import League, Team, Player

class LeagueListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = ['url', 'id', 'name', 'country', 'number_teams']


class TeamListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['url', 'id', 'name', 'city']


class PlayerListSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamListSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['url', 'id', 'name', 'position', 'team']


class TeamDetailSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.ReadOnlyField()

    class Meta:
        model = Team
        fields = ['url', 'id', 'name', 'city', 'championships_won', 'coach', 'number_players', 'players']


class PlayerDetailSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.SlugRelatedField(slug_field='name', queryset=Team.objects.all())

    class Meta:
        model = Player
        fields = ['url', 'id', 'name', 'age', 'position', 'appearance', 'team']


class LeagueDetailSerializer(serializers.HyperlinkedModelSerializer):
    teams = TeamListSerializer(read_only=True, many=True)
    current_champion = serializers.SlugRelatedField(read_only=True, slug_field='name')
    number_teams = serializers.ReadOnlyField()
    most_championships = serializers.ReadOnlyField()
    most_appearances = serializers.ReadOnlyField()

    class Meta:
        model = League
        fields = ['url', 'id', 'name', 'country', 'number_teams', 'current_champion', 'most_championships', 'most_appearances', 'teams']

class TeamNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    championships_won = serializers.IntegerField(required=False)
    coach = serializers.CharField(required=False)

    class Meta:
        model = Team
        fields = ['id', 'name', 'city', 'championships_won', 'coach']

class LeagueCreateUpdateSerializer(serializers.ModelSerializer):
    teams = TeamNestedSerializer(many=True)
    current_champion = serializers.SlugRelatedField(slug_field='name', queryset=Team.objects.all(), required=False)

    def get_or_create_teams(self,teams_data):
        teams = []

        for team_data in teams_data:
            team_id = team_data.pop('id', None)
            print(team_data)
            team, _ = Team.objects.get_or_create(id=team_id, defaults=team_data)
            teams.append(team)

        return teams

    def create(self, validated_data):
        teams_data = validated_data.pop('teams')
        league = League.objects.create(**validated_data)
        teams = self.get_or_create_teams(teams_data)
        league.teams.add(*teams)

        return league

    def update(self, instance, validated_data):
        teams_data = validated_data.pop('teams')
        League.objects.update(**validated_data)
        teams = self.get_or_create_teams(teams_data)
        instance.teams.set(teams)

        return instance

    class Meta:
        model = League
        fields = ['url', 'id', 'name', 'country', 'current_champion', 'teams']
