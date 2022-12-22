# Cria uma lista vazia para armazenar alienígenas 
aliens = []
# Cria 30 alienígenas verdes 
for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Mostra os 5 primeiros alienígenas x 
for alien in aliens[:5]:
    print(alien) 
    print("...")
# Mostra quantos alienígenas foram criados y 
    print("Total number of aliens: " + str(len(aliens)))