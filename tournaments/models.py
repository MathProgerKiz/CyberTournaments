from django.db import models
from django.contrib.auth.models import User

# Модель для игр
class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название игры")
    genre = models.CharField(max_length=100, verbose_name="Жанр игры")
    platform = models.CharField(max_length=100, verbose_name="Платформа")

    def __str__(self):
        return self.name


# Модель для турниров
class Tournament(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название турнира")
    description = models.TextField(verbose_name="Описание турнира", blank=True)
    start_date = models.DateTimeField(verbose_name="Дата и время начала турнира")
    end_date = models.DateTimeField(verbose_name="Дата и время окончания турнира")
    location = models.CharField(max_length=100, verbose_name="Место проведения")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="tournaments", verbose_name="Игра")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tournaments", verbose_name="Создатель")

    def __str__(self):
        return self.name


# Модель для команд
class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название команды")
    members = models.ManyToManyField(User, related_name="teams", verbose_name="Участники")
    tournaments = models.ManyToManyField(Tournament, related_name="teams", verbose_name="Турниры")

    def __str__(self):
        return self.name


# Модель для матчей
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="matches", verbose_name="Турнир")
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team_a", verbose_name="Команда A")
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team_b", verbose_name="Команда B")
    score_a = models.IntegerField(verbose_name="Счет команды A", default=0)
    score_b = models.IntegerField(verbose_name="Счет команды B", default=0)
    match_date = models.DateTimeField(verbose_name="Дата и время матча")

    def __str__(self):
        return f"{self.team_a} vs {self.team_b} - {self.tournament.name}"


# Модель для лиг
class League(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название лиги")
    tournaments = models.ManyToManyField(Tournament, related_name="leagues", verbose_name="Турниры")

    def __str__(self):
        return self.name
