# 16) Faça um programa para uma loja de tintas. O programa deverá //pedir o tamanho em metros
# quadrados da área a ser pintada//. Considere que a //cobertura da tinta é de 1 litro para cada 3 metros
# quadrados// e que //a tinta é vendida em latas de 18 litros//, que //custam R$ 80,00//. Informe ao usuário a
# //quantidades de latas de tinta a serem compradas// e o //preço total//.
import math

areaToPaint = float(input('Digite a área em m² a ser pintada: '))

canOfPaint = {
  "liters": 18,
  "coverageByLiter": 3, #in square meters
  "price": 80
}

amountCanOfPaint = (areaToPaint / canOfPaint["coverageByLiter"]) / canOfPaint["liters"]

# 'math.ceil' rounds the number to the next integer
totalPrice = math.ceil(amountCanOfPaint) * canOfPaint["price"]

print(f'Você vai precisar comprar {math.ceil(amountCanOfPaint)} latas de tinta para cobrir essa área, custando um total de R${totalPrice:.2f}')