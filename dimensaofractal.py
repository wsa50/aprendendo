import numpy as np
np.__version_

from decimal import Decimal
import sys


def main():

    file = input('Informe o nome do arquivo: ')
    n_lines = int(input('Informe a quantidade de linhas do arquivo: '))
    delta = int(input('Informe a escala: '))

    calcular_alturas(file,n_lines,delta) #Chamando a função calcular_alturas e passando o nome do arq e a qtd de linhas como parâmetro
    dimensao_fractal(file,n_lines,delta)

'''Função para calcular cada altura de um ponto ao outro e guardar em uma lista (sdf)'''

def update_delta(file,n_lines,soma):
    delta = int(input('Informe a nova escala: '))

    if(delta == -1):
        print('FIM DO PROGRAMA')
    else:        
        calcular_alturas(file,n_lines,delta) #Chamando a função calcular_alturas e passando o nome do arq e a qnt de linhas como parâmetro
        dimensao_fractal(file,n_lines,delta)

def calcular_alturas(file,n_lines,delta):

    x,y = np.loadtxt(file, unpack=True)    
    arquivo = open("alturas.data","w")    
    sdf=[]
    limite = int((n_lines / delta))
    
    for i in range(limite -1 ):

        xi=i*delta              #xi = 0 - delta = 10
        xf=xi+delta             #xf = 0 + 10 = 10

        deltaX=(x[xf]-x[xi])   # está lendo x[0]      deltaX= (x[10]-x[0])
        deltaY=(y[xf]-y[xi])

        sdf.append(np.sqrt(deltaX*deltaX+deltaY*deltaY))   #DL = |h(x[1])²+h(x[2])²|
        h = np.sqrt(deltaX*deltaX+deltaY*deltaY)
        h = Decimal(h)
        h = round(h,8) # Considerando apenas 8 casas decimais para o comprimento         
        
        arquivo.write(f'{i+1} {str(h)}\n') # Grava o valor das alturas em um arquivo chamado alturas.data

'''Função para calcular a soma de todas as alturas e calcular df'''
def dimensao_fractal(file,n_lines,delta):
    
    arquivo2 = open("relatorio.data","a") #Arquivo para gravar o delta e o comprimento   
    x,y = np.loadtxt("alturas.data", unpack=True)
    soma = sum(y) # Faz a soma mais rapido
    # for i in range(n_lines - 1):  
    #     soma = soma + y[i]
    

    print("\n           ############ Resultados ################\n")    
    print(f'Delta: {delta} Soma dos comprimentos: {soma}\n')

    
    
    arquivo2.write(f'{delta} {str(soma)}\n')
    
    if(delta != -1):
        update_delta(file,n_lines,soma)
        

# início da execução do programa
#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main
