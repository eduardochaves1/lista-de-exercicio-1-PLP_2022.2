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
# PS.: This algorithm will use the "math" lib with 'math.floor' to round the number to the previous integer and 'math.ceil' to round the number to the next integer

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


# these 2 variables below are been used to calculate the *exclusive* amount of Cans OR Gallons, in which are the first 2 points in this exercise
onlyAmountOfCan = math.ceil(amountOfPaint / canOfPaint["liters"])
onlyAmountOfGallon = math.ceil(amountOfPaint / gallonOfPaint["liters"])


# these 3 variables below are been used to calculate the amount of Cans AND Gallons, in which is the third point in this exercise
bothAmountOfCan = math.ceil(amountOfPaint) / canOfPaint["liters"]

# "amountOfPaintOverloaded" will help the algorithm to calculate the amount of Gallons needed to complete the amount of paint that the Can of paint couldn't fill
amountOfPaintOverloaded = (bothAmountOfCan - math.floor(bothAmountOfCan)) * canOfPaint["liters"]
bothAmountOfGallon = amountOfPaintOverloaded / gallonOfPaint["liters"]


# down below the algorithm is calculating the total price based on the amount of...
#  Cans OR Gallons needed
totalPriceCan = onlyAmountOfCan * canOfPaint["price"]
totalPriceGallon = onlyAmountOfGallon * gallonOfPaint["price"]

# Cans AND Gallons needed
totalPriceBoth = (math.floor(bothAmountOfCan) * canOfPaint["price"]) + (math.ceil(bothAmountOfGallon) * gallonOfPaint["price"])


print(f'- Você vai precisar comprar {onlyAmountOfCan} latas de tinta para cobrir esta área, custando um total de R${totalPriceCan:.2f}. Levando um total de {onlyAmountOfCan * canOfPaint["liters"]}L de tinta.')


print(f'- Ou {onlyAmountOfGallon} galões de tinta para cobrir esta área, custando um total de R${totalPriceGallon:.2f}. Levando um total de {onlyAmountOfGallon * gallonOfPaint["liters"]}L de tinta.')


print(f'- Ou {math.floor(bothAmountOfCan)} latas de tinta, mais {math.ceil(bothAmountOfGallon)} galões de tinta para cobrir esta área, custando um total de R${totalPriceBoth:.2f}. Levando um total de {(math.floor(bothAmountOfCan) * canOfPaint["liters"]) + (math.ceil(bothAmountOfGallon) * gallonOfPaint["liters"])}L de tinta.')


print('- O que você acha que vale mais apena? 🤔')