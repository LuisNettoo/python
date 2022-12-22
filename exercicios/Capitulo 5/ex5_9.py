users = ['admin', 'louis', 'sawken', 'eric', 'alice']

if users:

  for user in users:
        if user == 'admin':
            print('Olá {}, gostaria de ver um relatório de status?'.format(user))
        else:
            print('Olá {}, obrigado por fazer login novamente.'.format(user.title()))

else:
    print('Precisamos encontrar alguns usuários.')
