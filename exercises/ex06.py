# 6) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input('Digite o valor do Raio do círculo (cm): '))

area = math.pi * raio**2

print(f'A área do círculo de {raio:.2f}cm é de: {area:.2f}cm')