import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']

intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

heroes_int = []
for i in intelligence_dict.values():
    heroes_int.append(i)
max_int = max(heroes_int)

for name, intelligence in intelligence_dict.items():
    if intelligence == max_int:
        print(f'Самый умный супергерой - {name}')
