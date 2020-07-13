from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(AbstractUser):

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de creación'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='fecha de modificación'
    )

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']


class Championships(models.Model):

    TYPE_CHAMPIONSHIPS_CHOICE = (
        (1, 'Copa América 2021'),
        (2, 'Eurocopa 2021'),
        (3, 'Liga BetPlay'),
        (4, 'Copa Libertadores 2021'),
        (5, 'Copa Sudamericana 2021'),
        (6, 'Champions League 2021'),
        (7, 'Europa League 2021'),
        (8, 'Serie A'),
        (9, 'Liga Santander'),
        (10, 'Premier League'),
    )
    # project_type = models.CharField(max_length=100, choices=TYPE_CHAMPIONSHIPS_CHOICE)
    type_championships = models.PositiveSmallIntegerField(
        choices=TYPE_CHAMPIONSHIPS_CHOICE,
        default=1,
        verbose_name='tipo de campeonato'
    )

    creator = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        verbose_name='creador',
        null=True

    )

    description = models.TextField(
        verbose_name='descripción',
        blank=True
    )

    def __str__(self):
        return f'{self.get_type_championships_display()}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonatos'

class Phase(models.Model):
    TYPE_phase_CHOICE = (
        (1, 'grupos'),
        (2, 'semifinal'),
        (3, 'final'),
    )
    type_phase = models.PositiveSmallIntegerField(
        choices=TYPE_phase_CHOICE,
        default=1,
        verbose_name='Tipo de phase'
    )
    number_jornadas = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Numero de jornadas'
    )
    championships = models.ForeignKey(
        Championships,
        on_delete=models.CASCADE,
        verbose_name='campeonato'
    )

    def __str__(self):
        return f'{self.get_type_phase_display()} - {self.championships}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Fase'
        verbose_name_plural = 'Fases'


class Day(models.Model):


    date_time = models.DateField(
        verbose_name='fecha de la jornada'
    )
    number_day = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Numero de jornada'
    )

    phase = models.ForeignKey(
        Phase,
        on_delete=models.CASCADE,
        verbose_name='fase'
    )

    def __str__(self):
        return f'({self.number_day}, {self.date_time}) - {self.phase}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'


class Teams(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    image = models.FileField(upload_to='Logos')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'


class Match(models.Model):

    day = models.ForeignKey(
        Day,
        on_delete=models.CASCADE
    )

    local_team = models.ForeignKey(
        Teams,
        on_delete=models.SET_NULL,
        null=True,
        related_name='local_team'
    )
    visiting_team = models.ForeignKey(
        Teams,
        on_delete=models.SET_NULL,
        null=True,
        related_name='visiting_team'
    )

    winner = models.ForeignKey(
        Teams,
        on_delete=models.SET_NULL,
        verbose_name='ganador',
        blank=True,
        null=True
    )

    goals_local_team = models.PositiveSmallIntegerField(
        verbose_name='goles equipo local',
        blank=True,
        null=True
    )
    goals_visiting_team = models.PositiveSmallIntegerField(
        verbose_name='goles equipo visitante',
        blank=True,
        null=True
    )
    goals_penal_local_team = models.PositiveSmallIntegerField(
        verbose_name='goles penales equipo local',
        blank=True,
        null=True
    )
    goals_penal_visiting_team = models.PositiveSmallIntegerField(
        verbose_name='goles penales equipo visitante',
        blank=True,
        null=True
    )

    party_date = models.DateTimeField(
        verbose_name='fecha de partido'
    )

    def __str__(self):
        return f'{self.local_team} vs {self.visiting_team} - {self.day} - {self.day.phase} - {self.day.phase.championships}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'

