my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for my_food in my_foods:
    print('Minha comida favorita é {}'.format(my_food.title()))

for friend_food in friend_foods:
    print('A comida favorita do meu amigo é {}'.format(friend_food.title()))