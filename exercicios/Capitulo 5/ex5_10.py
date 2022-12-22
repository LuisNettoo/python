current_users = ['louis', 'sawken', 'eric', 'alice', 'dan']
new_users = ['louis', 'sawken', 'rafa', 'yan', 'gabi']

for new_user in new_users:
    
    if new_user in current_users:
        print('{} usuário indisponível, pois o nome já está sendo usado.'.format(new_user))
    else:
        print('{} está disponível e pronto para um novo registro'.format(new_user))
