person1 = {
    'first_name': 'danilo',
    'last_name': 'morais',
    'age': '18',
    'city': 'bjs',
}

person2 = {
    'first_name': 'marcos',
    'last_name': 'santos',
    'age': '19',
    'city': 'bjs',
}

person3 = {
    'first_name': 'micheal',
    'last_name': 'cirino',
    'age': '21',
    'city': 'slz',
}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print('{}: {}'.format(key, value.title()))
