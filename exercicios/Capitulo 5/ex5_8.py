users = ['admin', 'louis', 'sawken', 'eric', 'alice']

for user in users:
    if user == 'admin':
        print('Olá {}, gostaria de ver um relatório de status?'.format(user))
    else:
        print('Olá {}, obrigado por fazer login novamente.'.format(user.title()))
