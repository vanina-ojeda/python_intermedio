a = {1 , 3, 5, 7}
b = {3, 7, 9, 11}

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
#elementos que se encuentran en A o en B, o en ambos
union = a | b
print(f"union : {union}")

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
#elementos que se encuentran en A y en B
interseccion = a & b
print(f"interseccion :{interseccion}")

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
#conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
print(f"diferencia simetrica :{ a.symmetric_difference(b)}")

#Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es
#un subconjunto de otro conjunto, B.
print(f"es a un subconjunto de b ?:{a.issubset(b)}")

#Dados un conjunto, A, escribe un programa en Python que imprima el número de
#elementos del conjunto.
print(F"elementos que contiene el conjunto a : {len(a)}")