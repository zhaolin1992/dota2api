import json

from .hero import Hero
from .detail import Leaver, AbilityUpgrade, AdditionalUnit
from .item import load_item
from ..src.utils import load_json_file


with open(load_json_file("abilities.json")) as abilities_json:
    abilities = json.load(abilities_json)

with open(load_json_file("regions.json")) as regions_json:
    regions = json.load(regions_json)

with open(load_json_file("lobbies.json")) as lobbies_json:
    lobbies = json.load(lobbies_json)

with open(load_json_file("modes.json")) as modes_json:
    modes = json.load(modes_json)


class BasePlayer(object):
    def __init__(self, **kwargs):
        self.account_id = kwargs.get("account_id", -1)
        self.player_slot = kwargs["player_slot"]

        self.hero = Hero(kwargs["hero_id"])

        self.items = []
        self.items.append(load_item(0, **kwargs))
        self.items.append(load_item(1, **kwargs))
        self.items.append(load_item(2, **kwargs))
        self.items.append(load_item(3, **kwargs))
        self.items.append(load_item(4, **kwargs))
        self.items.append(load_item(5, **kwargs))

        self.kills = kwargs["kills"]
        self.deaths = kwargs.get("deaths", kwargs.get('death'))
        self.assists = kwargs["assists"]

        self.gold = kwargs["gold"]
        self.last_hits = kwargs["last_hits"]
        self.denies = kwargs["denies"]
        self.gold_per_min = kwargs["gold_per_min"]
        self.xp_per_min = kwargs["xp_per_min"]
        self.gold_spent = kwargs.get("gold_spent")
        self.hero_damage = kwargs.get("hero_damage")
        self.tower_damage = kwargs.get("tower_damage")
        self.hero_healing = kwargs.get("hero_healing")
        self.level = kwargs["level"]

    def __repr__(self):
        return 'Player account_id: {}'.format(self.account_id)


class Players(list):
    def __init__(self, **kwargs):
        super(Players, self).__init__()
        list(map(self.append, [Player(**summary_kwargs) for summary_kwargs in kwargs['players']]))


class Player(object):
    def __init__(self, **kwargs):
        self.steam_id = kwargs.get('steamid')
        self.community_visibility_state = kwargs.get('communityvisibilitystate')
        self.profile_state = kwargs.get('profilestate')
        self.persona_name = kwargs.get('personaname')
        self.last_logoff = kwargs.get('lastlogoff')
        self.profile_url = kwargs.get('profileurl')
        self.url_avatar = kwargs.get('avatar')
        self.url_avatar_medium = kwargs.get('avatarmedium')
        self.url_avatar_full = kwargs.get('avatarfull')
        self.persona_state = kwargs.get('personastate')
        self.primary_clan_id = kwargs.get('primaryclanid')
        self.time_created = kwargs.get('timecreated')
        self.persona_state_flags = kwargs.get('personastateflags')

    def __repr__(self):
        return 'Player steam_id: {} name: {}'.format(self.steam_id, self.persona_name)


class DetailedPlayer(BasePlayer):
    def __init__(self, **kwargs):
        super(DetailedPlayer, self).__init__(**kwargs)
        self.ability_upgrades = [AbilityUpgrade(**ability_upgrade_kwargs) for ability_upgrade_kwargs in
                                 kwargs.get("ability_upgrades", [])]
        self.additional_units = [AdditionalUnit(**additional_unit) for additional_unit in
                                 kwargs.get('additional_units', [])]
        if kwargs.get("leaver_status") is None:
            self.leaver_status = None
        else:
            self.leaver_status = Leaver(kwargs.get("leaver_status"))
