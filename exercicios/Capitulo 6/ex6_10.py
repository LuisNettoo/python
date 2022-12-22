cities = {
    'bonjas': {
                'country': 'brazil',
                'population': '37k',
                'fact': 'horrivel'
    },
    'borys': {
                'country': 'brazil',
                'population': '73k',
                'fact': 'pessima',
    },
    'rio': {
                'country': 'brazil',
                'population': '6kk',
                'fact': 'crime',
    },
}

for city, info in cities.items():
    if city == 'borys':
        print('\nInformações sobre a cidade de ' + city.title())
    else:
        print('\nInformações sobre a cidade do ' + city.title())
    for k, v in info.items():
        print('{}: {}'.format(k, v.title()))