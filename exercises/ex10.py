# 10) Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celcius = int(input('Digite a temperatura em Celcius: '))

fahrenheit = celcius * 9 / 5 + 32

print(f'Esta temperatura em Fahrenheit é {fahrenheit:.1f}°F')