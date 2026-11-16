# Caso 10: Llamadas internacionales

codigo = int(input("Ingrese el código de la zona: "))
minutos = float(input("Ingrese los minutos hablados: "))

if minutos < 0:
    print("La cantidad de minutos no es válida.")
elif codigo == 10:
    zona = "América del norte"
    precio = 2.2
elif codigo == 12:
    zona = "América del centro"
    precio = 2.5
elif codigo == 20:
    zona = "América del sur"
    precio = 1.2
elif codigo == 22:
    zona = "Asia"
    precio = 3.5
elif codigo == 30:
    zona = "Europa"
    precio = 3.0
elif codigo == 32:
    zona = "África"
    precio = 3.2
else:
    zona = ""
    precio = 0

if minutos >= 0 and zona != "":
    total = minutos * precio
    print("Zona llamada:", zona)
    print("Costo por minuto: S/", precio)
    print("Total a pagar: S/", round(total, 2))
elif minutos >= 0:
    print("El código ingresado no existe.")
