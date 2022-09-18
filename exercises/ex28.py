# 28) Faça um Programa que //pergunte em que turno você estuda//. Peça para digitar **M-matutino ou V-
# Vespertino ou N- Noturno**. Imprima a mensagem **"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor
# Inválido!"**, conforme o caso.

studyShift = input('+ Em qual turno você estuda? ["M" para matutino, "V" para vespertino ou "N" para noturno]: ')

if studyShift == 'M' or studyShift == 'm':
  print('Boa Tarde!')
elif studyShift == 'V' or studyShift == 'v':
  print('Bom Dia!')
elif studyShift == 'N' or studyShift == 'n':
  print('Boa Noite')
else:
  print('Valor Inválido!')