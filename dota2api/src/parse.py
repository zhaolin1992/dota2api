from .exceptions import APIError
from ..obj.match import DetailedMatch
from ..obj.live_game import LiveLeagueListing, LiveGames, TournamentPrizePool, Teams
from ..obj.history import HistoryMatches
from ..obj.player import Players
from ..obj.hero import Heroes
from ..obj.item import Items


def parse_result(result):
    if 'match_id' in result and 'radiant_win' in result:
        return DetailedMatch(**result)

    if 'matches' in result:
        return HistoryMatches(**result)

    if 'leagues' in result:
        return LiveLeagueListing(**result)

    if 'games' in result:
        return LiveGames(**result)

    if 'teams' in result:
        return Teams(**result)

    if 'players' in result:
        return Players(**result)

    if 'heroes' in result:
        return Heroes(**result)

    if 'items' in result:
        return Items(**result)

    if 'prize_pool' in result:
        return TournamentPrizePool(**result)

    raise APIError("There are no parser available for the result")
