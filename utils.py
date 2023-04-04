import json
from pprint import pprint


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    pprint(data)
    return data
