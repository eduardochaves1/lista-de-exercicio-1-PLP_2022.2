# 8) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

incomeByHour = float(input('Digite o valor da sua hora? R$'))
monthlyWorkingTime = int(input('Quantas horas você trabalhou neste mês? '))

print(f'Você ganhou R${monthlyWorkingTime * incomeByHour :.2f} neste mês')