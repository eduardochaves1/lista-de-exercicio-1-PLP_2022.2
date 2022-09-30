# 29) As Organizações PLP LTDA resolveram dar um aumento de salário aos seus colaboradores e lhe
# contraram para desenvolver **o programa que calculará os reajustes**. O reajuste acontecerá segundo o
# seguinte critério, **baseado no salário atual**:
# •  salários até R$ 280,00 (incluindo) : aumento de 20%
# •  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# •  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# •  salários de R$ 1500,00 em diante : aumento de 5%

# Após o aumento ser realizado informe na tela:
# •  o salário antes do reajuste;
# •  o percentual de aumento aplicado;
# •  o valor do aumento;
# •  o novo salário, após o aumento.

oldSalary = float(input('+ Digite o seu salário atual: R$'))

if oldSalary <= 280:
  percentageIncreased = 1.2
  salary = oldSalary * percentageIncreased

elif oldSalary > 280 and oldSalary <= 700:
  percentageIncreased = 1.15
  salary = oldSalary * percentageIncreased

elif oldSalary > 700 and oldSalary <= 1500:
  percentageIncreased = 1.1
  salary = oldSalary * percentageIncreased
  
else:
  percentageIncreased = 1.05
  salary = oldSalary * percentageIncreased

salaryIncreased = salary - oldSalary

print(f'- O salário antes do reajuste era de {oldSalary:.2f}')
print(f'- Novo salário será de R${salary:.2f}')
print(f'- O aumento foi de {(percentageIncreased - 1) * 100 :.0f}% (R${salaryIncreased:.2f}) em relação ao antigo salário')