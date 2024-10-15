from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from tournaments.serializers import (
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




