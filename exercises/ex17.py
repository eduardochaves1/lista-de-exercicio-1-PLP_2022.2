# 17) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6
# litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
# situações:

# •  comprar apenas latas de 18 litros;
# •  comprar apenas galões de 3,6 litros;
# •  misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
#    sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

areaToPaint = float(input('+ Digite a área em m² a ser pintada: '))

canOfPaint = {
  "liters": 18,
  "price": 80
}
gallonOfPaint = {
  "liters": 3.6,
  "price": 25
}

paintCoverageByLiter = 6 #in square meters
amountOfPaint = (areaToPaint / paintCoverageByLiter) * 1.1 # the "1.1" multiplication is for 10% addition in the calculation

onlyAmountOfCan = amountOfPaint / canOfPaint["liters"]
onlyAmountOfGallon = amountOfPaint / gallonOfPaint["liters"]

# 'math.floor' rounds the number to the previous integer
amountOfCan = math.ceil(amountOfPaint) / canOfPaint["liters"]
amountOfPaintOverloaded = (amountOfCan - math.floor(amountOfCan)) * canOfPaint["liters"]
amountOfGallon = amountOfPaintOverloaded / gallonOfPaint["liters"]

# 'math.ceil' rounds the number to the next integer
totalPriceCan = math.ceil(onlyAmountOfCan) * canOfPaint["price"]
totalPriceGallon = math.ceil(onlyAmountOfGallon) * gallonOfPaint["price"]
totalPriceBoth = (math.floor(amountOfCan) * canOfPaint["price"]) + (math.ceil(amountOfGallon) * gallonOfPaint["price"])

print(f'- Você vai precisar comprar {math.ceil(onlyAmountOfCan)} latas de tinta para cobrir esta área, custando um total de R${totalPriceCan:.2f}. Levando um total de {math.ceil(onlyAmountOfCan) * canOfPaint["liters"]}L de tinta.')

print(f'- Ou {math.ceil(onlyAmountOfGallon)} galões de tinta para cobrir esta área, custando um total de R${totalPriceGallon:.2f}. Levando um total de {math.ceil(onlyAmountOfGallon) * gallonOfPaint["liters"]}L de tinta.')

print(f'- Ou {math.floor(amountOfCan)} latas de tinta mais {math.ceil(amountOfGallon)} galões de tinta para cobrir esta área, custando um total de R${totalPriceBoth:.2f}. Levando um total de {(math.floor(amountOfCan) * canOfPaint["liters"]) + (math.ceil(amountOfGallon) * gallonOfPaint["liters"])}L de tinta.')

print('- O que você acha que vale mais apena? 🤔')