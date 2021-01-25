import pprint

capitals = {
    'France' : 'Paris',
    'Germany': 'Berlin',
    'Hungary': 'Budapest'
}

travel_log = {
    'France' : {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
    'Germany': {'cities_visited': ['Berlin', 'Stuttgart', 'Hamburg'], 'total_visits': 5},
    'Hungary': {'cities_visited': ['Budapest', 'Pécs', 'Debrecen', 'Szeged'], 'total_visits': 4}
}

pprint.pprint(travel_log)

my_travels = [
    {'date'    : '2019-02-12',
     'country' : 'Germany',
     'cities'  : ['Berlin', 'Stuttgart', 'Munich', 'Frankfurt'],
     'duration': '2w'
     },
    {'date'    : '2020-02-12',
     'country' : 'France',
     'cities'  : ['Paris', 'Dijon', 'Lille'],
     'duration': '1w'
     },
]

print('')
print('My travels:')
pprint.pprint(my_travels)

print('')
print('All visited cities:')
for travel in my_travels:
    for city in travel['cities']:
        print(city)
