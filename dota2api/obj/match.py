import json

from .player import DetailedPlayer
from ..src.utils import load_json_file


class DetailedMatch(object):
    def __init__(self, **kwargs):
        self.is_radiant_win = bool(kwargs["radiant_win"])
        self.duration = kwargs["duration"]
        self.start_time = kwargs["start_time"]
        self.match_id = kwargs["match_id"]
        self.match_seq_num = kwargs["match_seq_num"]
        self.tower_status_radiant = kwargs['tower_status_radiant']
        self.tower_status_dire = kwargs['tower_status_dire']
        self.barracks_status_radiant = kwargs['barracks_status_radiant']
        self.barracks_status_dire = kwargs['barracks_status_dire']
        self.cluster = kwargs['cluster']
        self.cluster_name = cluster_name(self.cluster)
        self.first_blood_time = kwargs['first_blood_time']
        self.lobby_type = kwargs['lobby_type']
        self.lobby_name = lobby_name(self.lobby_type)
        self.human_players = kwargs['human_players']
        self.league_id = kwargs['leagueid']
        self.positive_votes = kwargs['positive_votes']
        self.negative_votes = kwargs['negative_votes']
        self.game_mode = kwargs['game_mode']
        self.game_mode_name = game_mode_name(self.game_mode)

        self.players = [DetailedPlayer(**player_kwargs) for player_kwargs in kwargs['players']]

    def __repr__(self):
        return 'Match match_id: {}'.format(self.match_id)


def game_mode_name(mode_id):
    """
    Parse the lobby, will be available as ``game_mode_name``
    """
    return [mode['name'] for mode in modes['modes'] if mode['id'] == mode_id][0]


def lobby_name(lobby_id):
    """
    Parse the lobby, will be available as ``lobby_type``
    """
    return [lobby['name'] for lobby in lobbies['lobbies'] if lobby['id'] == lobby_id][0]


def cluster_name(region_id):
    """
    Parse the lobby, will be available as ``cluster_name``
    """
    return [region['name'] for region in regions['regions'] if region['id'] == region_id][0]


with open(load_json_file("regions.json")) as regions_json:
    regions = json.load(regions_json)

with open(load_json_file("lobbies.json")) as lobbies_json:
    lobbies = json.load(lobbies_json)

with open(load_json_file("modes.json")) as modes_json:
    modes = json.load(modes_json)
