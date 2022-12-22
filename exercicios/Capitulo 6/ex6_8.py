dog = {
    'cachorro': 'daniel',
}

cat = {
    'gato': 'luis',
}

parrot = {
    'papagaio': 'itallo'
}

pets = [dog, cat, parrot]

for pet in pets:
    for key, value in pet.items():
        print('{}: {}'.format(key, value.title()))