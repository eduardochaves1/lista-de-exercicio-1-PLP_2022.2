# 11) Faça um Programa que peça 2 números inteiros e um número real...

int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite outro número inteiro: '))
float1 = float(input('Por último, digite um número quebrado (dizíma, ex.: 2.55): '))

# Calcule e mostre:
# a.  o produto = do dobro do primeiro + com metade do segundo.
print(f'11a: {int1*2 * int2/2}')

# b.  a soma = do triplo do primeiro + com o terceiro.
print(f'11b: {int1*3 + float1}')

# c.  o terceiro elevado ao cubo.
print(f'11c: {float1**3 :.2f}')