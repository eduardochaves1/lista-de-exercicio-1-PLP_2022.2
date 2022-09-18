# 25) Faça um Programa que leia três números e mostre o maior e o menor deles.

biggestNumber = -9999

for i in range(1,4):
  n = int(input(f'+ [{i}] Digite um número inteiro: '))
  if n > biggestNumber:
    biggestNumber = n

print(f'- O maior número foi "{biggestNumber}"')