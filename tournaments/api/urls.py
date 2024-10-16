from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (GameViewSet, 
                    LeagueViewSet, 
                    MatchViewSet,
                    TeamViewSet, 
                    TournamentViewSet,
            )

router = DefaultRouter()
router.register(r'game', GameViewSet)  

router_league = DefaultRouter()
router.register(r'league', LeagueViewSet)  

router_match = DefaultRouter()
router.register(r'match', MatchViewSet)  

router_team = DefaultRouter()
router.register(r'team', TeamViewSet)  

router_tour = DefaultRouter()
router.register(r'tournament', TournamentViewSet)  


urlpatterns = [
    path('', include(router.urls)),  
    path('', include(router_league.urls)),
    path('', include(router_match.urls)),
    path('', include(router_team.urls)),
    path('', include(router_tour.urls)),
]