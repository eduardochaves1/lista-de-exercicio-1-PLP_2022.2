# 32) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a.  "Telefonou para a vítima?"
# b.  "Esteve no local do crime?"
# c.  "Mora perto da vítima?"
# d.  "Devia para a vítima?"
# e.  "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. //Se a
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita"//, //entre 3 e 4
# como "Cúmplice"// //e 5 como "Assassino"//. //Caso contrário, ele será classificado como "Inocente"//.
questionsMarked = 0
questions = [
  '+ Telefonou para a vítima? ',
  '+ Esteve no local do crime? ',
  '+ Mora perto da vítima? ',
  '+ Devia para a vítima? ',
  '+ Já trabalhou com a vítima? ',
]

print('i - Para todas as perguntas, responda "s" ou "n":')

for question in questions:
  answer = input(question)
  
  if answer == 's' or answer == 'S':
    questionsMarked += 1

if questionsMarked == 2:
  print('- Suspeito')
elif questionsMarked >= 3 and questionsMarked <= 4:
  print('- Cúmplice')
elif  questionsMarked == 5:
  print('- Assassino')
else:
  print('- Inocente')