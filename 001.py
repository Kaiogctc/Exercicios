from time import sleep
from random import randint
computador = randint(0,10)
print('Olá, sou seu computador...Acabei de pensar em um numero entre 0 a 10')
print('Sera que você consegue advinhar qual foi? Escolha um nivel e explicarei as regras ')
niveljog = int(input('''[ 1 ] Fácil
[ 2 ] Médio
[ 3 ] Difícil
Em qual nivel deseja jogar? '''))
while niveljog not in range(1, 4):
    niveljog = int(input('Opa, não entendi coloque de novo sua escola de 1 a 3: '))
if niveljog == 1:
    print('Nesse nível você vai jogar até acertar, no final mostrarei o numero de tentativas')
    contador = 0
    jogador = int(input('Qual seu palpite? '))
    while computador != jogador:
        contador += 1
        if jogador < computador:
            print('Mais... Tente mais um vez')
            jogador = int(input('Qual seu palpite? '))
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
            jogador = int(input('Qual seu palpite? '))
        while jogador not in range(0, 10):
            jogador = int(input('Opa, não entendi coloque de novo sua escola de 0 a 10: '))
    print(f'VOCÊ ACERTOU!!\nCom {contador+1} tentativas')
if niveljog == 2:
    print('No nivel 2 "Médio" você terá apenas 3 chances de acertar! ')
    contador2 = 0
    jogador1 = int(input('Qual seu palpite? '))
    while jogador1 != computador and contador2 < 2:
        if jogador1 < computador:
            contador2 += 1
            print('Mais... tente mais uma vez')
            jogador1 = int(input('Qual seu palpite? '))
        if jogador1 > computador:
            contador2 += 1
            print('Menos... tente mais uma vez')
            jogador1 = int(input('Qual seu palpite? '))
    if contador2 == 2 and jogador1 != computador:
        print('Você excedeu as suas 3 chances, GAME OVER!!')
        print(f'O numero é {computador}')
    if jogador1 == computador:
        print(f'VOCÊ ACERTOU!!Com {contador2} chance/s')
    print(jogador1, contador2)
if niveljog == 3:
    print('Nesse nível, eu (Maquina), serei seu oponente! Boa sorte ')
    contadorpc = 0
    c = 's'
    contador = 0
    while c == 's':
        computador = randint(0, 10)
        print(computador)
        jogador = int(input('Escolha um numero entre 0 e 10 : '))
        while jogador not in range(0, 10):
            jogador = int(input('Opa, não entendi coloque de novo sua escolha de 0 a 10: '))
        print('Lendo seu pensamento...')
        sleep(1.0)
        if jogador == computador:
            sleep(0.7)
            print('VOCÊ ACERTOU!')
            contador += 1
            sleep(0.7)
        else:
            sleep(0.7)
            print(f'Sabia que você ia errar... eu pensei no numero {computador}')
            contadorpc += 1
            sleep(0.7)

        print(f'O placar está {contador} para você e {contadorpc} para mim')
        sleep(1)
        c = str(input('Para jogar novamente Tecle [ S ]\nPara Desistir Tecle [ N ]')).lower()
    if contadorpc > contador:
        print('Até mais, na próxima tente um adversário humano...')
    else:
        print('Até mais, na próxima ganharei de você')
