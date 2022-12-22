pizzas = ['calabresa', 'frango', 'margerita']

friend_pizzas = pizzas[:]

friend_pizzas.append('queijo')

for pizza in pizzas:
    print('Eu gosto muito da pizza de ' + pizza.title())

for friend_pizza in friend_pizzas:
    print('Meu amigo ama pizza de ' + friend_pizza.title())

print('Eu realmente adoro pizza!')