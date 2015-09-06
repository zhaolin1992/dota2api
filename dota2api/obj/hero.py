import json

from ..src import urls
from .item import load_item
from ..src.utils import load_json_file


class Heroes(list):
    def __init__(self, **kwargs):
        super(Heroes, self).__init__()
        list(map(self.append, [Hero(hero_kwargs['id']) for hero_kwargs in kwargs['heroes']]))


class Hero(object):
    def __init__(self, hero_id):
        self.id = hero_id
        hero_json_map = hero_map(hero_id)
        if hero_json_map:
            self.localized_name = hero_json_map['localized_name']
            self.name = hero_json_map['name']
            internal_name = self.name.replace('npc_dota_hero_', '')
            base_images_url = urls.BASE_HERO_IMAGES_URL + internal_name

            self.url_small_portrait = base_images_url + '_sb.png'
            self.url_large_portrait = base_images_url + '_lg.png'
            self.url_full_portrait = base_images_url + '_full.png'
            self.url_vertical_portrait = base_images_url + '_vert.jpg'
        else:
            self.localized_name = ''
            self.name = ''
            self.url_small_portrait = ''
            self.url_large_portrait = ''
            self.url_full_portrait = ''
            self.url_vertical_portrait = ''

    def __repr__(self):
        return 'Item id: {} name: {}'.format(self.id, self.localized_name)


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


def ability_name(ability_id):
    ability = [ability['name'] for ability in abilities['abilities'] if ability['id'] == str(ability_id)]
    if ability:
        return ability[0]
    else:
        return "UNKNOWN"


def hero_map(hero_id):
    """
    Parse the the hero name, will be available as ``hero_name``
    """

    hero_maps = [hero for hero in heroes['heroes'] if hero['id'] == hero_id]
    if hero_maps:
        return hero_maps[0]
    else:
        return None


with open(load_json_file("leaver.json")) as items_json:
    items = json.load(items_json)

with open(load_json_file("abilities.json")) as abilities_json:
    abilities = json.load(abilities_json)

with open(load_json_file("heroes.json")) as heroes_json:
    heroes = json.load(heroes_json)