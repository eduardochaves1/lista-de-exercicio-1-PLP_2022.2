# 31) Faça um programa para o //cálculo de uma folha de pagamento//, sabendo que os descontos são do
# **Imposto de Renda**, que depende do **salário bruto** (conforme tabela abaixo) e **3% para o
# Sindicato** e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa
# que deposita). O //Salário Líquido corresponde ao Salário Bruto menos os descontos//. O programa
# deverá **pedir ao usuário o valor da sua hora** e a **quantidade de horas trabalhadas no mês**.

# Desconto do IR:
# •  Salário Bruto até 900 (inclusive)  - isento
# •  Salário Bruto até 1500 (inclusive) - desconto de 5%
# •  Salário Bruto até 2500 (inclusive) - desconto de 10%
# •  Salário Bruto acima de 2500        - desconto de 20%

# **Imprima na tela as informações, dispostas conforme o exemplo abaixo**. No exemplo o valor da hora
# é 5 e a quantidade de hora é 220.

# - Salário Bruto: (5 * 220): R$ 1100,00
# - (-) IR (5%): R$ 55,00
# - (-) INSS ( 10%): R$ 110,00
# - FGTS (11%): R$ 121,00
# - Total de descontos: R$ 165,00
# - Salário Liquido: R$ 935,00

fgts = 1.11
inss = 1.1
workedHours = int(input('+ Quantas horas você trabalha por mês? '))
hourValue = int(input('+ Quanto vale a sua hora? R$'))
bruteSalary = hourValue * workedHours

if bruteSalary <= 900:
  ir = 1
elif bruteSalary > 900 and bruteSalary <= 1500:
  ir = 1.05
elif bruteSalary > 1500 and bruteSalary <= 2500:
  ir = 1.1
else:
  ir = 1.2

totalFees = bruteSalary * (inss + ir - 1) - bruteSalary
netSalary = bruteSalary - totalFees

print(f'- Salário Bruto: R${bruteSalary:.2f}')
print(f'- INSS ({(inss - 1) * 100:.0f}%): R${(bruteSalary * inss) - bruteSalary :.2f}')
print(f'- IR ({(ir - 1) * 100:.0f}%): R${(bruteSalary * ir) - bruteSalary :.2f}')
print(f'- FGTS ({(fgts - 1) * 100:.0f}%): R${(bruteSalary * fgts) - bruteSalary :.2f}')
print(f'- Total de Descontos: R${totalFees:.2f}')
print(f'- Salário Líquido: R${netSalary:.2f}')