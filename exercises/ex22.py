# 22) Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vowels = ('a', 'e', 'i', 'o', 'u')
letter = input('Digite uma letra: ')

if letter in vowels:
  print(f'A letra "{letter}" é vogal!')
else:
  print(f'A letra "{letter}" é consoante!')