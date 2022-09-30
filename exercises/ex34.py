# 34) Faça um programa que //cadastre o **nome**, a **altura**, o **peso**, o **cpf** e **sexo**
# de **algumas pessoas**//. Com os dados cadastrados, em seguida //localizar uma pessoas através
# do seu CPF e imprimir o seu **IMC**//. Obs.: //Solicitar ao usuário se deseja cadastrar mais
# pessoas ou parar.//
people = {}

while True:
  print('====== MENU ======')
  print('1 - Cadastrar Pessoa')
  print('2 - Pesquisar um Cadastro')
  print('3 - Listar Dados de uma Pessoa')
  print('4 - Parar')
  menuChoice = int(input('\n ? Digite o número de sua escolha: '))

  if menuChoice == 1:
    # cadastrar uma pessoa no dicionário
    name = input(f'\n + Digite o nome da pessoa: ')
    height = float(input(f'+ Digite a altura da pessoa [ex.: 1.67]: '))
    weight = float(input(f'+ Digite o peso da pessoa [ex.: 52.3]: '))
    cpf = int(input(f'+ Digite o CPF da pessoa [somente números]: '))
    sex = input(f'+ Digite o sexo da pessoa [f/m]: ')

    imc = weight / height**2

    people.update({cpf : {"name": name, "height": height, "weight": weight, "sex": sex, "imc": imc}})

  elif menuChoice == 2:
    # consultar uma pessoa no dicionário
    cpfSearch = int(input('\n ? Digite o CPF da pessoa que desaja saber o IMC: '))
    personName = people[cpfSearch]["name"]
    personIMC = people[cpfSearch]["imc"]
    print(f'- O IMC de {personName} (CPF: {cpfSearch}) é de {personIMC:.1f}')

  elif menuChoice == 3:
    # printar os dados de uma pessoa no dicionário
    print(f'\n {people}')

  else:
    # finalizar o código
    print('\n - Até a próxima!')
    break