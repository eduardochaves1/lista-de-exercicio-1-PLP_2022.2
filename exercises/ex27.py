# 27) Faça um Programa que leia três números e mostre-os em ordem decrescente.

numbers = []

for i in range(1,4):
  numbers.append(float(input(f'+ Digite um número real: ')))

numbers.sort()
print(numbers)