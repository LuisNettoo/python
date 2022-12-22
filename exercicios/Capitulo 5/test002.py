print('='*15)
print('     ENTRAR ')
print('='*15)

users = ['sawken']
passwords = ['12345']

user = str(input('Digite seu usuário: '))


if user.lower() == users[0]:
    password = str(input('Agora digite sua senha: '))
    if password == passwords[0]:
        print('Login bem-sucedido!')
    else:
        print('Senha incorreta. Tente novamente!')
else:
    print('Usuário incorreto. Tente novamente!')
