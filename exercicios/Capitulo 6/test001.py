users = {}

users['user'] = str(input('Digite seu usuário: '))
users['password'] = str(input('Digite sua senha: '))

print(users)

users['user'] = str(input('Digite seu novo usuário: '))

print(users)

del users['password']

print(users)