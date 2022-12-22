from random import randint
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']

computador = randint(0, 2)

print('='*20)
print(' '*5, 'JOKENPO')
print('='*20)
print('[0] Pedra\n[1] Papel\n[2] Tesoura')
print('='*20)

jogador = int(input('Escolha o que você irá jogar: '))

sleep(1)
print('Pedra...')

sleep(1)
print('Papel...')

sleep(1)
print('E Tesoura...')
sleep(1)

if computador == 0 and jogador == 2:
    print('O computador escolheu {} e você escolheu {}'.format(lista[computador], lista[jogador]))
    print('Você perdeu!!!')

elif computador == 1 and jogador == 0:
    print('O computador escolheu {} e você escolheu {}'.format(lista[computador], lista[jogador]))
    print('Você perdeu!!!')

elif computador == 2 and jogador == 1:
    print('O computador escolheu {} e você escolheu {}'.format(lista[computador], lista[jogador]))
    print('Você perdeu!!!')

elif computador == 0 and jogador == 1:
    print('O computador escolheu {} e você escolheu {}'.format(lista[computador], lista[jogador]))
    print('Você ganhou!!!')

elif computador == 1 and jogador == 2:
    print('O computador escolheu {} e você escolheu {}'.format(lista[computador], lista[jogador]))
    print('Você ganhou!!!')

elif computador == 2 and jogador == 0:
    print('O computador escolheu {} e você escolheu {}'.format(lista[computador], lista[jogador]))
    print('Você ganhou!!!')

else:
    print('O computador escolheu {} e você escolheu {}'.format(lista[computador], lista[jogador]))
    print('Empatou')
