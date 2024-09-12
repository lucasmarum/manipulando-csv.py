import csv

with open(r'C:\Users\lucas\numeros.csv', 'w') as arquivo:
    #cria objeto de gravação
    writer = csv.writer(arquivo)
    #grava arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63, 87, 92))
    writer.writerow((61, 79, 76))
    writer.writerow((72, 64, 91))
with open(r'C:\Users\lucas\numeros.csv', 'r', encoding='utf8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for item in leitor:
        print(item)