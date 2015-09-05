import json

from ..src.utils import load_json_file
from ..src.urls import BASE_ITEMS_IMAGES_URL


with open(load_json_file("abilities.json")) as abilities_json:
    abilities = json.load(abilities_json)

with open(load_json_file("regions.json")) as regions_json:
    regions = json.load(regions_json)

with open(load_json_file("lobbies.json")) as lobbies_json:
    lobbies = json.load(lobbies_json)

with open(load_json_file("modes.json")) as modes_json:
    modes = json.load(modes_json)

with open(load_json_file("items.json")) as items_json:
    items = json.load(items_json)


def item_map(item_id):
    item_maps = [item for item in items['items'] if item['id'] == item_id]

    if item_maps:
        return item_maps[0]
    else:
        return ''


def load_item(index, **kwargs):
    live_game_item_index = "item" + str(index)
    match_history_item_index = "item_" + str(index)

    item_id = kwargs.get(match_history_item_index, kwargs.get(live_game_item_index))
    return Item(item_id)


class Items(list):
    def __init__(self, **kwargs):
        super(Items, self).__init__()
        list(map(self.append, [Item(item_kwargs['id']) for item_kwargs in kwargs['items']]))


class Item(object):
    def __init__(self, item_id):
        item_json_map = item_map(item_id)
        self.id = item_id
        if item_json_map:
            self.localized_name = item_json_map['localized_name']
            self.name = item_json_map['name']
            self.is_recipe = bool(item_json_map['recipe'])
            self.in_secret_shop = bool(item_json_map['secret_shop'])
            self.cost = item_json_map['cost']
            self.in_side_shop = bool(item_json_map['side_shop'])
            self.url_image = BASE_ITEMS_IMAGES_URL + self.name.replace('item_', '') + '_lg.png'
        else:
            self.localized_name = ''
            self.name = ''
            self.is_recipe = False
            self.in_secret_shop = False
            self.cost = 0
            self.in_side_shop = 0
            self.url_image = ''

    def __repr__(self):
        return 'Item id: {} name: {}'.format(self.id, self.localized_name)