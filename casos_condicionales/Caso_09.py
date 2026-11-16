# Caso 9: Compra de camisas

cantidad = int(input("¿Cuántas camisas va a comprar? "))
precio = float(input("Ingrese el precio de cada camisa: S/ "))

if cantidad <= 0 or precio < 0:
    print("Ingrese una cantidad y un precio válidos.")
else:
    total = cantidad * precio

    if cantidad <= 4:
        porcentaje = 0.125
    elif cantidad <= 8:
        porcentaje = 0.20
    else:
        porcentaje = 0.315

    descuento = total * porcentaje
    pago = total - descuento

    print("Compra sin descuento: S/", round(total, 2))
    print("Descuento: S/", round(descuento, 2))
    print("Compra con descuento: S/", round(pago, 2))
