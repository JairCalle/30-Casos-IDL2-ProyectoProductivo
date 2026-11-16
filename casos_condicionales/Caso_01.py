# Caso 1: Precio de llantas

cantidad = int(input("¿Cuantas llantas va a comprar? "))

if cantidad <= 0:
    print("Ingrese una cantidad valida.")
else:
    if cantidad < 5:
        precio = 150
    else:
        precio = 120

    total = cantidad * precio
    print("Precio por llanta: S/", precio)
    print("Total a pagar: S/", total)
