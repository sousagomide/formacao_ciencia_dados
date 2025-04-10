import numpy as np

def amplitude(lista):
    lista_ordenada = np.sort(np.array(lista))
    return lista_ordenada[-1] - lista_ordenada[0]

def string_vert(string):
    for i in string:
        print(i)


print(amplitude([5, 10, 1, 3, 7, 2]))
string_vert('Alvim')



