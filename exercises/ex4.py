# 4) Faça um Programa que peça as 4 notas bimestrais e mostre a média.

sumgrade = 0
for bimonth in range(1,5):
  grade = float(input(f'+ Digite a nota do seu {bimonth}º Bimestre (ex.: 9 ou 9.5): '))
  sumgrade += grade

print('↓')
print(f'= Sua média dos 4 Bimestres foi de {sumgrade / 4:.2f} pontos')