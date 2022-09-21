# 19) Crie um programa para preencher um vetor (lista) com números inteiros e solicitar um número do
# teclado. Pesquisar se esse número existe no vetor. Se existir, imprimir em qual posição do vetor (lista)
# foi digitado. Se não existir, imprimir mensagem que não existe.

numbers = []

for number in range(1,11):
  numbers.append(int(input(f'+ [{number}º] Digite um número de 0 à 9: ')))

nChecks = int(input('\n + Quantos números você quer verificar na lista? '))

for check in range(1,nChecks+1):
  verifyNumber = int(input(f'\n ? Digite o {check}º número a ser verificado: '))

  if numbers.count(verifyNumber) > 0:
    print(f' - Este número está presente no Index {numbers.index(verifyNumber)} da lista')
  else:
    print(' - Este número não está presente na lista.')