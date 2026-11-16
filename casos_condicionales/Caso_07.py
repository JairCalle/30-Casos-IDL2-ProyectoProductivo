# Caso 7: Pago de una llamada

minutos = float(input("Ingrese la duración de la llamada en minutos: "))

if minutos <= 0:
    print("Ingrese una duración válida.")
else:
    costo = 0
    restante = minutos

    # Primeros cinco minutos: S/ 1.00 cada uno
    if restante > 5:
        costo = costo + 5 * 1.00
        restante = restante - 5
    else:
        costo = costo + restante * 1.00
        restante = 0

    # Siguientes tres minutos: S/ 0.80 cada uno
    if restante > 0:
        if restante > 3:
            costo = costo + 3 * 0.80
            restante = restante - 3
        else:
            costo = costo + restante * 0.80
            restante = 0

    # Siguientes dos minutos: S/ 0.70 cada uno
    if restante > 0:
        if restante > 2:
            costo = costo + 2 * 0.70
            restante = restante - 2
        else:
            costo = costo + restante * 0.70
            restante = 0

    # Desde el minuto diez en adelante: S/ 0.50 cada uno
    if restante > 0:
        costo = costo + restante * 0.50

    domingo = input("¿La llamada fue en domingo? (s/n): ").lower()
    nocturno = input("¿Fue en turno nocturno? (s/n): ").lower()

    if domingo == "s" and nocturno == "s":
        porcentaje = 0.05  # Domingo en turno nocturno
    elif domingo == "s":
        porcentaje = 0.03  # Domingo en otro turno
    else:
        porcentaje = 0

    impuesto = costo * porcentaje
    total = costo + impuesto

    print("Costo de la llamada: S/", round(costo, 2))
    print("Impuesto: S/", round(impuesto, 2))
    print("Total a pagar: S/", round(total, 2))
