# 9) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = int(input('Digite a temperatura em Fahrenheit: '))

celcius = 5 * ((fahrenheit - 32) / 9)

print(f'Esta temperatura em Celsius é {celcius:.1f}°C')