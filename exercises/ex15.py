# 15) Faça um Programa que pergunte quanto você //ganha por hora// e o //número de horas trabalhadas
# no mês//. Calcule e mostre o //total = do seu salário no referido mês//, sabendo-se que são descontados
# -11% para o Imposto de Renda, -8% para o INSS e -5% para o sindicato, faça um programa que nos dê:

# a.  salário bruto.
# b.  quanto pagou ao INSS.
# c.  quanto pagou ao sindicato.
# d.  o salário líquido.
# e.  calcule os descontos e o salário líquido, conforme a tabela abaixo

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido.

incomeTax = .11
inssTax = .08
syndicteTax = .05

incomeByHour = float(input('+ Digite o valor da sua hora? R$'))
monthlyWorkingTime = int(input('+ Quantas horas você trabalhou neste mês? '))

salary = incomeByHour + monthlyWorkingTime
print(f'Seu salário é de R${salary:.2f}')

netIncomeTax = salary * incomeTax
print(f'O valor descontado por conta do IR é de R${netIncomeTax:.2f}')

netInssTax = salary * inssTax
print(f'O valor descontado por conta do INSS é de R${netInssTax:.2f}')

netSyndicteTax = salary * syndicteTax
print(f'O valor descontado por conta do sindicato é de R${netSyndicteTax:.2f}')

netSalary = salary - netIncomeTax - netInssTax - netSyndicteTax
print(f'O seu salário líquido no final das contas é de R${netSalary:.2f}')