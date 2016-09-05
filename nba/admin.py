from django.contrib import admin

from nba.models import Team, Player


class TeamAdmin(admin.ModelAdmin):
    search_fields =('name',)

class PlayerAdmin(admin.ModelAdmin):
    search_fields =('name',)


admin.site.register(Team,TeamAdmin)
admin.site.register(Player,PlayerAdmin)

