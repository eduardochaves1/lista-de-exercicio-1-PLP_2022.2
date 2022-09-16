# 20) Faça um programa que exiba na tela a //quantidade de acertos -- de cada aluno// em uma prova, e
# //caso a *nota* seja igual ou maior >= que *60% da quantidade de questões* exiba “Classificado”, se não
# “Desclassificado”//. Para isso crie uma TUPLA que receba o cartão gabarito com as 20 questões, cada
# uma com cinco alternativas identificadas por A, B, C, D e E., Depois crie uma lista para cada Aluno e
# receba as 20 questões da prova dele e diga se o aluno está Classificado ou Desclassificado. //Ao final,
# pergunte se o usuário deseja cadastrar outro aluno ou finalizar o programa.//

# Obs.: Utilizar os conceitos vistos em sala de (Tupla, Lista, Estrutura Condicionais e Repetições);

# eu poderia ter feito um loop para inputar cada resposta do bagarito, mas por preguiça preferi deixar já declarado mesmo rsrs
answers = ('C','B','D','B','D','A','A','B','B','A','C','A','A','D','D','E','B','C','D','C')
studentAnswers = []
rightAnswers = 0
continueRegistration = True

while continueRegistration == True:
  print('Atênção! Digite apenas letras maiúsculas, ex.: A, B, C, D, E!')
  arrayIndex = -1

  for studentAnswer in answers:
    arrayIndex += 1
    studentAnswers.append(input(f'+ Digite a resposta do aluno para a {arrayIndex+1}º questão: '))
    
    if studentAnswers.__getitem__(arrayIndex) == answers.__getitem__(arrayIndex):
      rightAnswers += 1

  if rightAnswers == len(answers):
    print('Esse aí deve ter filado ein...')
  elif rightAnswers >= (len(answers) * .6):
    print('- O aluno está Classificado!')
  else:
    print('- O aluno está Desclassificado')

  continueChoice = input('? Você deseja cadastrar outro aluno [s/n]? ')

  if continueChoice == 's' or continueChoice == 'S':
    studentAnswers.clear()
    rightAnswers = 0
    print()
  else:
    print('Até a próxima!')
    continueRegistration = False