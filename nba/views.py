# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from nba.models import Team, Player


def index(request):
    if request.GET.get('sort_by') == 'quantity':
        return stat_by_player_quantity(request)

    elif request.GET.get('sort_by') == 'height':
        return stat_by_player_height(request)

    elif request.GET.get('sort_by') == 'experience':
        return stat_by_player_experience(request)

    else:#по умолчанию, при первой загрузке
        return stat_by_player_quantity(request)



def stat_by_player_quantity(request):
    teams = Team.objects.all()
    number_of_teams = len(teams)
    averageByTeams = [] #teamname teamCity av_property

    # importance - относительное значение по приоритетy от 3 до 6
    e_i = 4.5 #exp_importance
    h_i = 4.9 #height_importance
    g_i = 5.3 #goals_importance

    for team in teams:
        experience_list = [p.experience for p in team.player_set.all()]
        height_list = [p.height for p in team.player_set.all()]
        goal_list = [p.goals for p in team.player_set.all()]

        # "качество" * "коэффициент" / ("сколько значений в тиблице" * "количество команд")
        rel_exp = sum(experience_list) * e_i / (len(experience_list) * number_of_teams)
        rel_height = sum(height_list) * h_i / (len(height_list) * number_of_teams)
        rel_goals = sum(goal_list) * g_i / (len(goal_list) * number_of_teams)


        #для сортировки команд в таблице получим среднее качество по выбраным свойствам
        av_property = round(sum([rel_exp, rel_height, rel_goals])/3,1)


        averageByTeams.append([team.name, team.city, av_property])


    if request.is_ajax():
        teams_list = [team[0] for team in averageByTeams]
        average_quantity = [team[2] for team in averageByTeams]

        return JsonResponse({'teams':teams_list,'quantity':average_quantity})
    else:
        #сортировка списка по убываю для рейтинговой таблицы
        averageByTeams.sort(key=lambda av_list: av_list[2],reverse=True)
        teams = [(team[0],team[1]) for team in averageByTeams]

        return render(request,'nba/statistics.html',{'teams':teams})



def stat_by_player_height(request):
    teams = Team.objects.all()
    averageByTeams = [] #[teamName,teamCity,averageHeightInTeam]

    for team in teams:
        #получаем список роста по командам
        height_list = [p.height for p in team.player_set.all()]

        averageByTeams.append([team.name,team.city,sum(height_list)/len(height_list)])


    if request.is_ajax():
        teams_list = [team[0] for team in averageByTeams]
        average_height = [team[2] for team in averageByTeams]

        return JsonResponse({'teams':teams_list,'height':average_height})

    else:
        #сортировка списка по убываю для рейтинговой таблицы
        averageByTeams.sort(key=lambda av_list: av_list[2],reverse=True)
        teams = [(team[0],team[1]) for team in averageByTeams]

        return render(request,'nba/statistics.html',{'teams':teams})



def stat_by_player_experience(request):
    teams = Team.objects.all()
    averageExpByTeams = [] #[teamName,teamCity,averageHeightInTeam]

    for team in teams:
        #получаем список опыта по командам
        exp_list = [p.experience for p in team.player_set.all()]
        averageExpByTeams.append([team.name,team.city,sum(exp_list)/len(exp_list)])


    if request.is_ajax():
        teams_list = [team[0] for team in averageExpByTeams]
        average_exp = [team[2] for team in averageExpByTeams]

        return JsonResponse({'teams':teams_list,'exp':average_exp})

    else:
        #сортировка списка по убываю для рейтинговой таблицы
        averageExpByTeams.sort(key=lambda av_list: av_list[2],reverse=True)
        teams = [(team[0],team[1]) for team in averageExpByTeams]

        return render(request,'nba/statistics.html',{'teams':teams})
