# 14) João Papo-de-Pescador, homem de bem, comprou um computador para controlar o //rendimento
# diário// de seu trabalho. Toda vez que ele traz um //peso de peixes// >>maior que o //estabelecido// pelo
# regulamento de pesca do estado de São Paulo (==50 quilos) ::deve pagar uma multa de R$ 4,00 por
# quilo excedente::. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e ++calcule o excesso++. Gravar na variável excesso a quantidade de quilos além do limite e na
# variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
# mensagens adequadas.

maxWeight = 50
overloadFee = 4

weightAcumulated = float(input('Diga lá João Papo-de-Pescador, quantos kg tu pegou de peixe hoje? '))

if weightAcumulated > maxWeight:
  fineAmount = (weightAcumulated - maxWeight) * overloadFee
  print(f'É Jão caba vei... hoje tu vai ter que pagar R${fineAmount:.2f} de multa por ter passado dos 50kg')
else:
  print('Se safou hoje caba vei... Tu não vai ter que pagar multa nenhuma kk...')