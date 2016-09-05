# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from nba.models import Team, Player



def index(request):
    if request.GET.get('sort_by') == "height":
        return stat_by_player_height(request)

    elif request.GET.get('sort_by') == "experience":
        return stat_by_player_experience(request)

    #по умолчанию при первой загрузке
    else:
        return stat_by_player_height(request)


def stat_by_player_height(request):
    players = Player.objects.select_related('team').order_by('height')

    #получение уникальных ID из игроков команды
    teams_id_list = set([p.team.id for p in players])

    #сортировка по макимальному росту
    teams_id_list = reversed(list(teams_id_list))

    #получение команд в порядке сортировки по весу(по убыванию веса)
    teams =  [Team.objects.get(id=ind) for ind in teams_id_list]

    return render(request,'nba/statistics.html',{'teams':teams})


def stat_by_player_experience(request):
    players = Player.objects.select_related('team').order_by('experience')

    #получение уникальных ID из игроков команды
    teams_id_list = [p.team.id for p in players]
    for i in teams_id_list:
        if teams_id_list.count(i)>1: teams_id_list.remove(i)


    #получение команд в порядке сортировки по весу(по убыванию опыта)
    teams =  [Team.objects.get(id=ind) for ind in teams_id_list]

    return render(request,'nba/statistics.html',{'teams':teams})

