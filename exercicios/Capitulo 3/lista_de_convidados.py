pessoas = ['Bill', 'Megan', 'Forever']

print(pessoas[0] + ', quer jantar comigo?')
print(pessoas[1] + ', quer jantar comigo?')
print(pessoas[2] + ', quer jantar comigo?\n')

print('É parece que {} não vai poder comparecer \n'.format(pessoas[2]))

pessoas.pop()

print(pessoas[0] + ', quer jantar comigo?')
print(pessoas[1] + ', quer jantar comigo?\n')

print('Encontrei uma mesa maior vou convidar novas pessoas!!\n')

pessoas.append('Bolsonaro')
pessoas.append('Lula')
pessoas.append('Ciro')

print(pessoas)

print(pessoas[0], 'você está convidada ao meu jantar')
print(pessoas[1], 'conto com sua presença no jantar')
print(pessoas[2], 'aguardo você no jantar')
print(pessoas[3], 'espero que você compareça')
print(pessoas[4], 'está mais que convidado para o jantar\n')

print(len(pessoas))

sorry1 = pessoas.pop()
print('{}, desculpa por cancelar o jantar!'.format(sorry1))

sorry2 = pessoas.pop()
print('{}, desculpa mas não temos mais uma mesa que comporte todos'.format(sorry2))

sorry3 = pessoas.pop()
print('{}, não posso mais levar você para o jantar\n'.format(sorry3))

del pessoas[0]
del pessoas[0]

print(pessoas)

print(len(pessoas))


