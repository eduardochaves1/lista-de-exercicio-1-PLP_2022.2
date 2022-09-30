# 34) Faça um programa que //cadastre o **nome**, a **altura**, o **peso**, o **cpf** e **sexo**
# de **algumas pessoas**//. Com os dados cadastrados, em seguida //localizar uma pessoas através
# do seu CPF e imprimir o seu **IMC**//. Obs.: //Solicitar ao usuário se deseja cadastrar mais
# pessoas ou parar.//
people = {}


# register a person on the people dict
def registerPerson (cpf):
  name = input(f'+ Digite o nome da pessoa: ')
  height = float(input(f'+ Digite a altura da pessoa [ex.: 1.67]: '))
  weight = float(input(f'+ Digite o peso da pessoa [ex.: 52.3]: '))
  sex = input(f'+ Digite o sexo da pessoa [f/m]: ')

  imc = round(weight / height**2, 1) # the "1" after the calculus is to round the result with only one float digit

  people.update({cpf : {"name": name, "height": height, "weight": weight, "sex": sex, "imc": imc}})


# prints out the person's data from the people dict
def printPersonData (cpfSearch):
  personName = people[cpfSearch]["name"]
  personHeight = people[cpfSearch]["height"]
  personWeight = people[cpfSearch]["weight"]
  personSex = people[cpfSearch]["sex"]
  personIMC = people[cpfSearch]["imc"]

  if personSex == "m" or personSex == "M":
    personSex = "Másculino"
  elif personSex == "f" or personSex == "F":
    personSex = "Feminino"
  else:
    personSex = "Null"

  print(f'- CPF: {cpfSearch} | Nome: {personName} | Altura: {personHeight} | Peso: {personWeight} | Sexo: {personSex} | IMC: {personIMC}')


while True:
  print('\n====== MENU ======')
  print('1 - Cadastrar Pessoa')
  print('2 - Listar Dados de uma Pessoa')
  print('3 - Parar')
  menuChoice = int(input('\n? Digite o número de sua escolha: '))

  if menuChoice == 1:
    cpf = int(input(f'\n+ Digite o CPF da pessoa [somente números]: '))

    if cpf in people:
      updateChoice = int(input('! Este CPF já foi cadastrado! Se desejas consultá-lo digite "1"; Se desejas alterá-lo digite "2"; Ou se desejas voltar digite "3": '))
      if updateChoice == 1:
        printPersonData(cpf)
      elif updateChoice == 2:
        registerPerson(cpf)
    else:
      registerPerson(cpf)


  elif menuChoice == 2:
    cpfSearch = int(input('\n? Digite o CPF da pessoa que desaja consultar [somente números]: '))

    while cpfSearch not in people:
      errorChoice = int(input('! Este CPF não está cadastrado! Se desejas cadastrá-lo digite "1". Se desejas pesquisar por outro CPF digite "2". Ou se desejas voltar digite "3": '))
      if errorChoice == 1:
        registerPerson(cpfSearch)
      elif errorChoice == 2:
        cpfSearch = int(input('\n? Digite o CPF da pessoa que desaja consultar [somente números]: '))
        if cpfSearch in people:
          printPersonData(cpfSearch)
          break
      else:
        break

    else:
      printPersonData(cpfSearch)


  else:
    # ends the code
    print('\n- Até a próxima!')
    break