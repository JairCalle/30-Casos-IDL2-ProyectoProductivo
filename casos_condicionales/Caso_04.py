# Caso 4: Pago de colegiatura

materias = int(input("¿Cuántas materias lleva? "))
promedio = float(input("Ingrese su promedio del último periodo: "))

if materias <= 0:
    print("Ingrese una cantidad válida de materias.")
else:
    total = materias * 100  # Cada materia cuesta S/ 100

    if promedio >= 18:
        descuento = total * 0.25  # 50% de descuento aplicado a la mitad de los cursos
    else:
        descuento = 0

    pago = total - descuento
    print("Colegiatura sin descuento: S/", round(total, 2))
    print("Descuento: S/", round(descuento, 2))
    print("Total a pagar: S/", round(pago, 2))
