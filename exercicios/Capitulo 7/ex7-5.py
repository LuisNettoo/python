while True:
    age = input('Digite sua idade: ')
    if age == 'quit':
        break
    if age != 'quit':
        age = int(age)
    if age <= 3:
        print('Seu ingresso é gratuito')
    if 3 < age <= 12:
        print('Seu ingresso custará 10 dólares')
    if age > 12:
        print('Seu ingresso custará 15 dólares') 