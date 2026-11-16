# Caso 3: Cálculo del impuesto

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: S/ "))

if edad > 18 and ingresos >= 3000:
    impuesto = ingresos * 0.05  # El impuesto es el 5% del ingreso
    print("Le corresponde tributar.")
    print("Monto a pagar: S/", round(impuesto, 2))
else:
    print("No le corresponde tributar.")
