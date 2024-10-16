

from Cyber.tournaments.models import Tournament


def get_tournament_by_time(date):

    return  Tournament.objects.filter(start_date = date)

    