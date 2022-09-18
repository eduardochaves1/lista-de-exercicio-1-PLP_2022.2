# 23) Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular
# a média alcançada por aluno e apresentar:
# •  A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# •  A mensagem "Reprovado", se a média for menor do que sete;
# •  A mensagem "Aprovado com Distinção", se a média for igual a dez.

grade = int(input('Digite a nota do aluno: '))

if grade == 10:
  print('Aluno Aprovado com Distinção!')
elif grade >= 7:
  print('Aluno Aprovado!')
else:
  print('Aluno Reprovado!')