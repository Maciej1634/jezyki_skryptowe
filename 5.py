from random import randint
lista = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
lista_liter = [x[0] for x in lista]
lista_liczb = [randint(1, 10) for x in range(4)]
print(lista_liter)
print(lista_liczb)
