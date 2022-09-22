# 34) Faça um programa que //cadastre o **nome**, a **altura**, o **peso**, o **cpf** e **sexo**
# de **algumas pessoas**//. Com os dados cadastrados, em seguida //localizar uma pessoas através
# do seu CPF e imprimir o seu **IMC**//. Obs.: //Solicitar ao usuário se deseja cadastrar mais
# pessoas ou parar.//
people = {}

personOrder = 0
proceedRegristration = True
while proceedRegristration == True:
  personOrder += 1
  name = input(f'\n + [{personOrder}] Digite o nome da pessoa: ')
  height = float(input(f'+ [{personOrder}] Digite a altura da pessoa [ex.: 1.67]: '))
  weight = float(input(f'+ [{personOrder}] Digite o peso da pessoa [ex.: 52.3]: '))
  cpf = int(input(f'+ [{personOrder}] Digite o CPF da pessoa [somente números]: '))
  sex = input(f'+ [{personOrder}] Digite o sexo da pessoa [f/m]: ')

  imc = weight / height**2

  people.update({cpf : {"name": name, "height": height, "weight": weight, "sex": sex, "imc": imc}})

  proceedChoice = input('\n ? Desejas cadastrar outra pessoa [s/n]? ')
  if proceedChoice == 'n' or proceedChoice == 'N':
    proceedRegristration = False

while True:
  cpfSearch = int(input('\n ? Digite o CPF da pessoa que desaja saber o IMC: '))
  personName = people[cpfSearch]["name"]
  personIMC = people[cpfSearch]["imc"]
  print(f'- O IMC de {personName} (CPF: {cpfSearch}) é de {personIMC:.1f}')

  proceedChoice = input('\n ? Desejas pesquisar sobre o IMC de outra pessoa [s/n]? ')
  if proceedChoice == 'n' or proceedChoice == 'N':
    print('- Até a próxima!')
    break