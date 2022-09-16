# 21) Faça um programa que //peça do usuário o nome de 6 cidades//, depois de inseridas //verifique se há
# nomes iguais e havendo peça para que sejam inseridos novamente//, e também //crie a opção do usuário
# concatenar dados ao nome da cidade//. E por fim, //exiba qual o nome de cidade mais extenso//.

cities = []

for city in range(1,7):
  cities.append(dict(input(f'+ Digite o nome da {city}ª cidade: ')))

print(cities)

# still finishing...