# 26) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
# comprar, sabendo que a decisão é sempre pelo mais barato.
lowestPrice = 9999

print('i: Você pode digitar números inteiros ou reais ex.: "2" ou "2.55"')
for i in range(1,4):
  productPrice = float(input(f'+ Digite o preço do {i}º produto: R$'))
  if productPrice < lowestPrice:
    lowestPrice = productPrice

print(f'- Você deveria comprar o produto de R${lowestPrice:.2f}')