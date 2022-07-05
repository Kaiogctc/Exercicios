print('Esquerda numeros impares e direita numeros pares')
c = 0
while c < 100:
    c += 1
    if c % 2 == 0:
        print(f'{c}',end=' ')
    else:
        print(f'\n{c}',end='     ')


