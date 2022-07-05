# 2010  12%  \ acima de 2010 7% desconto
dinheiro= 0
pergunta = 'S'
desconto1 = 0
desconto2 = 0
while pergunta == 'S':
    ano = int(input('Qual ano de fabricação do seu carro? '))
    dinheiro = float(input('quanto custa o seu carro? '))
    desconto1 = dinheiro * 0.12
    desconto2 = dinheiro * 0.07
    if ano <= 2010:
        print(f'O desconto foi de R${desconto1}')
    else:
        print(f'O desconto foi de R${desconto2}')
    pergunta = str(input('deseja continuar? \nDigite [S] para continuar ou [N] para encerrar: ')).upper()

print('Encerrado')