# encoding: utf-8
from tastypie.resources import ModelResource, fields
from nba.models import Team, Player
from django.db import IntegrityError


class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = 'team'
        include_resource_uri = False
        excludes = ["id"]

    def determine_format(self, request):
        return 'application/json'

    def obj_create(self, bundle,**kwargs):
        name = bundle.data['name']
        city = bundle.data['city']

        try:
            bundle.obj = Team(name=name,city=city)
            bundle.obj.save()
        except IntegrityError:
            raise IntegrityError("That team already exist")

        return bundle


class PlayerResource(ModelResource):
    class Meta:
        queryset = Player.objects.all()
        resource_name = 'player'
        include_resource_uri = False
        excludes = ["id","player"]

    def determine_format(self, request):
        return 'application/json'

    #переопределяем вывод поля team:
    #вместо ссылки - название команды
    def dehydrate(self, bundle):
        try:
            player = Player.objects.filter(id=bundle.obj.id)
            bundle.data['team'] = player[0].team
        except Player.DoesNotExist:
            pass
        return bundle

    def obj_create(self, bundle,**kwargs):
        name = bundle.data['name']
        age = bundle.data['age']
        team = bundle.data['team']
        height = bundle.data['height']
        experience = bundle.data['experience']
        goals = bundle.data['goals']

        try:

            teams = Team.objects.filter(name=team)

            if teams:
                team = teams[0]
            else:
                raise ValueError("No team with that name exist")

            player = Player.objects.create(name=name,
                                        age=age,
                                        team=team,
                                        height=height,
                                        experience=experience,
                                        goals=goals)

        except IntegrityError:
            raise ValueError("That player already exist")

        return bundle

