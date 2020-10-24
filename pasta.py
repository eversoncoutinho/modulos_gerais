import os #modulo com varias funcoes de manipulacao de pasta
#criando n pastas pastas
'''n = str(input("digite a quantidade de pastas"))
for i in range(1,n):
    dir = './{:02d}_01_18'.format(i) #nome da pasta
    os.makedirs(dir) #criador de diretório
'''

source = 'arqui/'

lista = os.listdir(source)