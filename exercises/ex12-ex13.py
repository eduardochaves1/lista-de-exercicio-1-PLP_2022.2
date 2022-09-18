# 12) Tendo como dados de entrada a altura de uma pessoa, construa um programa que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# 13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
# peso ideal, utilizando as seguintes fórmulas:
# a.  Para homens: (72.7*h) - 58
# b.  Para mulheres: (62.1*h) - 44.7

sex = input('Qual seu sexo [f/m]? ')
altura = float(input('Digite sua altura em metros (ex.: 1.65): '))

if sex == 'f' or sex == 'F':
  idealWeight = 62.1 * altura - 44.7
else:
  idealWeight = 72.7 * altura - 58

print(f'Seu peso ideal é de {idealWeight:.2f}kg')