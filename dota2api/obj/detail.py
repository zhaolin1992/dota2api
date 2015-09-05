from .item import load_item
from .hero import *
from ..src.utils import load_json_file


with open(load_json_file("abilities.json")) as abilities_json:
    abilities = json.load(abilities_json)

with open(load_json_file("regions.json")) as regions_json:
    regions = json.load(regions_json)

with open(load_json_file("lobbies.json")) as lobbies_json:
    lobbies = json.load(lobbies_json)

with open(load_json_file("modes.json")) as modes_json:
    modes = json.load(modes_json)


class AbilityUpgrade(object):
    def __init__(self, **kwargs):
        self.ability = kwargs['ability']
        self.ability_name = ability_name(self.ability)
        self.time = kwargs['time']
        self.level = kwargs['level']

    def __repr__(self):
        return 'AbilityUpgrade ability: {} name: {} level: {}'.format(self.ability, self.ability_name, self.level)


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


class Leaver(object):
    def __init__(self, player_id):
        leaver = leaver_map(player_id)
        self.id = leaver['id']
        self.name = leaver['name']
        self.description = leaver['description']


def leaver_map(leaver_id):
    return [l for l in leavers if l['id'] == leaver_id][0]


with open(load_json_file("leaver.json")) as leaver_json:
    leavers = json.load(leaver_json)
