import numpy as np

def llenado(cn):
    matr = np.zeros((cn,cn))
    for f in range(cn):
        for c in range(cn):
            matr[f][c] = np.random.randint(1,255)
    return matr

def buscabit(sistema,cn):
    num_cumplen = []
    nub = 16
    for f in range(cn):
        for c in range(cn):
            if(int(sistema[f][c]&nub == 0):
               data = sistema[f][c]
               num_cumplen.append(data)
    return num_cumplen

n = int(input("ingrese el numero de filas del arreglo:"))
arr2 = llenado(n)
listado = buscabit(arr2,n)
print("numeros que cumplen\n",listado)
