from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('-= *11')
print('computador jogou{}'.format(itens[computador]))
print('jogador jogou{}'.format(itens[jogador]))
print('-= *11')
if computador ==0:# computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADOR INVÁLIDA!')