commands = {
    'insert': 'apagar um elemento de uma lista',
    'range': 'criar uma sequencia de numeros',
    'if': 'função que trabalha com condições',
    'for': 'cria um laço e acessa todos os itens de uma lista',
    'pop': 'remove um elemento de uma lista, mas o guarda em uma variavel',
    'sorted': 'ornaganiza os itens de uma lista em ordem alfabetica',
    'set': 'quando usar um laço para uma lista esse metodo faz com que valores repetidos só apareçam uma vez',
    'values': 'acessa somente os valores de um dicionario',
    'keys': 'acessa somente as chaves de um dicionario',
    'tittle': 'transforma a primeira letra de uma string em maiuscula',
}

for key, value in commands.items():
    print('\n{}: {}'.format(key, value))