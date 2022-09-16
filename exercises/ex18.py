# 18) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
# um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
# este link (em minutos)

fileSize = float(input('+ Digite o tamanho do arquivo em MB: '))
internetSpeed = int(input('+ Digite a velocidade da Internet em MBps: '))

estimatedTime = (fileSize / internetSpeed) / 60

print(f'- O tempo estimado de download deste arquivo é de {estimatedTime:.1f} minutos')