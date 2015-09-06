import json

from .hero import Hero
from .item import load_item
from ..src.utils import load_json_file


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


class Leaver(object):
    def __init__(self, player_id):
        leaver = leaver_map(player_id)
        self.id = leaver['id']
        self.name = leaver['name']
        self.description = leaver['description']


class AdditionalUnit(object):
    def __init__(self, **kwargs):
        self.unit_name = kwargs['unitname']
        self.items = []
        self.items.append(load_item(0, **kwargs))
        self.items.append(load_item(1, **kwargs))
        self.items.append(load_item(2, **kwargs))
        self.items.append(load_item(3, **kwargs))
        self.items.append(load_item(4, **kwargs))
        self.items.append(load_item(5, **kwargs))


class AbilityUpgrade(object):
    def __init__(self, **kwargs):
        self.ability = kwargs['ability']
        self.ability_name = ability_name(self.ability)
        self.time = kwargs['time']
        self.level = kwargs['level']

    def __repr__(self):
        return 'AbilityUpgrade ability: {} name: {} level: {}'.format(self.ability, self.ability_name, self.level)


def leaver_map(leaver_id):
    return [l for l in leavers if l['id'] == leaver_id][0]


def ability_name(ability_id):
    ability = [ability['name'] for ability in abilities['abilities'] if ability['id'] == str(ability_id)]
    if ability:
        return ability[0]
    else:
        return "UNKNOWN"


with open(load_json_file("leaver.json")) as leaver_json:
    leavers = json.load(leaver_json)

with open(load_json_file("abilities.json")) as abilities_json:
    abilities = json.load(abilities_json)