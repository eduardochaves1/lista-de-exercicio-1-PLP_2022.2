# 19) Crie um programa para preencher um vetor (lista) com números inteiros e solicitar um número do
# teclado. Pesquisar se esse número existe no vetor. Se existir, imprimir em qual posição do vetor (lista)
# foi digitado. Se não existir, imprimir mensagem que não existe.

numbers = []

for number in range(1,11):
  numbers.append(input(f'+ [{number}º] Digite um número de 0 à 9: '))

nChecks = int(input('+ Quantos números você quer verificar na lista? '))
print()

for check in range(1,nChecks+1):
  number = input(f'? Digite o {check}º número a ser verificado: ')

  if numbers.count(number) > 0:
    print(f'- Este número está presente no index {numbers.index(number)} da lista')
  else:
    print('- Este número não está presente na lista.')
  
  print()