sandwich_orders = ['atum', 'mortadela', 'presunto', 'queijo']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

for finish_sandwich in finished_sandwiches:
    print("Seu sanduíche de {} está pronto".format(finish_sandwich))