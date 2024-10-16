from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from Cyber.tournaments.api.serializers import (
    GameSerializers, 
    LeagueSerializers,
    MatchSerializers, 
    TeamSerializers, 
    TournamentSerializers,
)
from tournaments.models import (
    Game,
    League,
    Match, 
    Team, 
    Tournament,
)

@extend_schema(tags=['Game'])
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializers

@extend_schema(tags=['League'])
class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializers

@extend_schema(tags=['Match'])
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializers

@extend_schema(tags=['Team'])
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializers

@extend_schema(tags=['Tournament'])
class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializers

    @action(detail=True, methods=['get'])
    def tournament_date(self,request):
        """Данный метод выводит все турниры которые начинаются в определенное время"""
        return  Response({'tournament':Tournament.objects.filter(start_date = request.date)})





