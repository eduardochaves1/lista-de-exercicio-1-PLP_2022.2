# 24) Faça um Programa que leia três palavras e mostre a maior palavra entre eles, além de apresentar
# quantos caracteres tem na palavra.

biggestString = ''

for i in range(1,4):
  string = input(f'+ [{i}] Digite uma palavra: ')
  print(f'- Esta palavra tem {len(string)} letras')
  if len(string) > len(biggestString):
    biggestString = string

print(f'\n - A maior de todas as palavras foi "{biggestString}" com {len(biggestString)} letras')