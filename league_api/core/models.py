from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    championships_won = models.IntegerField(default=0)
    coach = models.CharField(max_length=200)

    @property
    def number_players(self):
        return Player.objects.filter(team=self).count()

    @property
    def players(self):
        return Player.objects.filter(team=self).values_list('name', flat=True)


class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    position = models.CharField(max_length=200)
    appearance = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class League(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    current_champion = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="fk_l_t_cc", null=True)
    teams = models.ManyToManyField(Team, blank=True)

    @property
    def number_teams(self):
        return self.teams.count()

    @property
    def most_championships(self):
        result = self.teams.filter(championships_won__gt=0).order_by("-championships_won")
        if result.count() > 0:
            return result[0].name
        else:
            return None

    @property
    def most_appearances(self):
        result = Player.objects.raw("SELECT 1 as id, c.name as name FROM core_player c JOIN core_team t ON(c.team_id = t.id) " \
            "JOIN core_league_teams lt ON(t.id = lt.team_id) WHERE lt.league_id = %s and c.appearance > 0 ORDER BY appearance DESC LIMIT 1",
            [self.id])
        if result:
            return result[0].name
        else:
            return None
