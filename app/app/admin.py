from django.contrib import admin

# Register your models here.
from app import models
from django.contrib.auth.admin import UserAdmin

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {'fields': (
                'username',
                'password',
                'email',
                'is_staff',
                'is_active',
                'is_superuser',
                'groups',
                )
            }
        ),
    )
    list_display = ('username', 'email', 'is_staff','is_superuser')


@admin.register(models.Championships)
class ChampionshipsAdmin(admin.ModelAdmin):
    list_display = ('type_championships','creator','description')


@admin.register(models.Phase)
class PhaseAdmin(admin.ModelAdmin):
    list_display = ('type_phase', 'championships', 'number_jornadas')


@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'phase')


@admin.register(models.Teams)
class TeamsAdmin(admin.ModelAdmin):
    # list_display = ('day', 'local_team', 'visiting_team', 'winner', 'goals_local_team', 'goals_visiting_team', 'goals_penal_local_team', 'goals_penal_visiting_team', 'party_date')
    list_display = ('pk','name', 'image')

@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('day', 'local_team', 'visiting_team', 'winner', 'goals_local_team', 'goals_visiting_team', 'goals_penal_local_team', 'goals_penal_visiting_team', 'party_date')
    # list_display = ('pk',)