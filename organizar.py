import os,sys #modulo com varias funcoes de manipulacao de pasta
#criando n pastas pastas

from time import sleep

source = str(input('Pasta(deixe vazio se o programa estiver na mesma pasta das fotos): '))
source.strip('/')
lista = os.listdir(source) #gera uma lista
print(lista)
sleep(10)
local = str(input('Local: '))

#print(len(lista))#contagem de itens na lista
for i in lista:
    ajuste=i.split('_')[1]
    new_name= local+'_'+ajuste
    os.rename(source+'/'+i,source+'/'+new_name)
print("Mudança realizada com sucesso")
#print(dir(lista))