sandwich_orders = ['atum', 'pastrami','mortadela', 'pastrami','presunto', 'pastrami' ,'queijo']
print('A lanchonete não está servindo sanduíche de pratami. Desculpa!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nA lanchonete tem esses sanduíches listados a baixo: \n")
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())
