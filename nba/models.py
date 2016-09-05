# encoding: utf-8
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=70,unique=True)
    city = models.CharField(max_length=150)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=200,unique=True)
    age = models.PositiveIntegerField()
    team = models.ForeignKey(Team)
    height = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    goals = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


