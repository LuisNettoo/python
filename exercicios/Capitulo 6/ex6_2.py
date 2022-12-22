favorite_numbers = {
    'dan': ['7', '14', '13'],
    'alice': ['13', '1', '8'],
    'noah': ['3', '5', '4'],
    'charles': ['8', '25', '64'],
    'monica': ['7', '6', '99'],
}

for name, numbers in favorite_numbers.items():
    print('Os numeros favoritos de {} são:'.format(name.title()))
    for number in numbers:
        print('\t' + number)