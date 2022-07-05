cont1 = 0
contm = 0
contf = 0
while True:
    print(' CADASTRE UMA PESSOA ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    pergunta = str(input('Quer continuar? [S/N]  ')).upper()
    if idade > 18:
        cont1 += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F'and idade < 20:
        contf += 1
    if pergunta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont1}')
print(f'Ao todo temos {contm}  homens cadastrados')
print(f'E temos {contf} mulheres com menos de 20 anos cadastradas')
