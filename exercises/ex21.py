# 21) Faça um programa que //peça do usuário o nome de 6 cidades//, depois de inseridas //verifique se há
# nomes iguais e havendo peça para que sejam inseridos novamente//, e também //crie a opção do usuário
# concatenar dados ao nome da cidade//. E por fim, //exiba qual o nome de cidade mais extenso//.

cities = {}
nRegristrations = int(input('+ Digite quantas cidades você quer cadastrar: '))
biggestName = ''

for city in range(0,nRegristrations):
  cityInput = input(f'+ Digite o nome da {city+1}ª cidade: ')

  if cityInput in cities:
    while True:
      cityInput = input('! Esta cidade já foi registrada, digite o nome de outra cidade: ')
      if cityInput not in cities:
        break
  
  if len(cityInput) > len(biggestName):
    biggestName = cityInput
  
  # this method down below will add a new key (city) inside our "cities" dictionary, with a blank string value
  cities.update({cityInput: ''})

  wannaAddInfo = input('? Você deseja adicionar alguma informação sobre essa cidade [s/n]? ')
  if wannaAddInfo == 's' or wannaAddInfo == 'S':
    # this method down below will add a value inside the last key (city) added in the "cities" dict
    cities.update({cityInput: input(f'+ Digite a informação que você deseja adicionar à cidade de {cityInput}: ')})


print(f'\n - A cidade com o maior nome foi {biggestName}')
print(cities)