# 33) Faça um programa que //cadastre o **nome**, a **matrícula** e **duas notas** de **13 alunos**//.
# Em seguida //imprima a **matrícula**, o **nome** e a **média** de **cada um deles**//.

students = {}
nStudents = int(input('? Quantos alunos deseja cadastrar? '))

for student in range(0, nStudents):
  print()
  name = input(f'+ Digite o nome do {student+1}º estudante: ')
  enrollment = input(f'+ Digite a matrícula do {student+1}º estudante: ')
  grade1 = int(input(f'+ Digite a 1º nota do {student+1}º estudante: '))
  grade2 = int(input(f'+ Digite a 2º nota do {student+1}º estudante: '))

  students.update({enrollment : {"name": name, "grade1": grade1, "grade2": grade2,}})

print()
for student in students:
  name = students[student]['name']
  avarage = (students[student]['grade1'] + students[student]['grade2']) / 2
  print(f'- O aluno {name} de matrícula {student} teve uma média de {avarage}')