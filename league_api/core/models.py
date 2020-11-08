from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    championships_won = models.IntegerField()
    coach = models.CharField(max_length=200)
    number_players = models.IntegerField()


class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    position = models.CharField(max_length=200)
    appearance = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class League(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    number_teams = models.IntegerField()
    current_champion = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="fk_l_t_cc", null=True)
    most_championships = models.ForeignKey(Team, on_delete=models.DO_NOTHING,  related_name="fk_l_t_mc", null=True)
    most_appearances = models.ForeignKey(Player, on_delete=models.DO_NOTHING, null=True)
    teams = models.ManyToManyField(Team, blank=True)
