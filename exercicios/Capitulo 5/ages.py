age = int(input('Qual sua idade? '))

if age < 2:
    print('Você é um bebê.')
elif 2 <= age < 4:
    print('Você é uma criança.')
elif 4 <= age < 13:
    print('Você é um(a) garoto(a).')
elif 13 <= age < 20:
    print('Você é um(a) adolescente.')
elif 20 <= age < 65:
    print('Você é um adulto.')
else:
    ('Voce é um(a) idoso(a).')