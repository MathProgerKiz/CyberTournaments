from rest_framework import serializers

from tournaments.models import (
    Game,
    League,
    Match, 
    Team, 
    Tournament,
)

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class TournamentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
class MatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__' 

class LeagueSerializers(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'