numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
          'oito', 'nove', 'dez', 'onze', 'doze','treze', 'cartoze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

continuar = 0
numero2 = int(input('Digite um numero entre 0 e 20: '))
while numero2 > 20 or numero2 < 0:
  numero2 = int(input('Tente novamente! Digite um numero entre 0 e 20: '))
print(f'Você digitou {numero[numero2]}')

