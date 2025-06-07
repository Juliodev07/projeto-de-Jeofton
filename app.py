from random import randint
itens = ('pedra', 'papel', 'tesoura')
while True:
    computador = randint(0, 2)
    print('''\nSuas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
    try:
        jogador = int(input('Qual é a sua jogada? '))
    except ValueError:
        print('Entrada inválida! Digite um número entre 0 e 2.')
        continue
    if jogador not in [0, 1, 2]:
        print('JOGADA INVÁLIDA!')
        continue
    print('-=' * 11)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 11)
    if computador == jogador:
        print('EMPATE')
    elif (computador == 0 and jogador == 1) or \
         (computador == 1 and jogador == 2) or \
         (computador == 2 and jogador == 0):
        print('JOGADOR VENCE')
    else:
        print('COMPUTADOR VENCE')
    resposta = input('\nDeseja jogar novamente? (s/n): ').strip().lower()
    if resposta != 's':
        print('Obrigado por jogar! Até a próxima.')
        break
