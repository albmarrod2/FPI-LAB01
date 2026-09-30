edad = int(input("Introduce tu edad: "))
n_fisico = int(input("Introduce tu nivel fisico del 1 al 10: "))
if edad < 18:
    print("Debes ser mayor de edad")
else:
    while n_fisico not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        n_fisico = int(input("Porfavor introduzca un numero del 1 al 10: "))
    if n_fisico < 5:
        print("Debes estar en mejor forma")
    else:
        print("¡Listo para despegar!")