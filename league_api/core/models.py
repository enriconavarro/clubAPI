from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=3)
    date_created = models.DateField()
    mascot = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


class Player(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
