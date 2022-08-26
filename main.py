#Escribe un programa que sea capaz de mostrar
# los números del 1 al 100 en orden inverso.

rango = range(1, 101)

for i in reversed(rango):
    print(f"- {i}")