# 7) Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lenght = float(input('Digite o valor da base do quadrado: '))
height = float(input('Digite o valor da altura do quadrado: '))

print(f'A área deste quadrado é de {lenght * height :.2f}')
print(f'O dobro desta área é de {lenght * height * 2 :.2f}')