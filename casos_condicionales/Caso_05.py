# Caso 5: Tipo de triángulo

lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Los lados deben ser mayores que cero.")
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Los lados no forman un triángulo.")
elif lado1 == lado2 and lado2 == lado3:
    perimetro = lado1 + lado2 + lado3
    print("El triángulo es equilátero.")
    print("Perímetro:", perimetro)
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
    if lado1 == lado2:
        print("Los lados iguales son:", lado1, "y", lado2)
    elif lado1 == lado3:
        print("Los lados iguales son:", lado1, "y", lado3)
    else:
        print("Los lados iguales son:", lado2, "y", lado3)
else:
    # Fórmula de Herón para calcular el área
    semiperimetro = (lado1 + lado2 + lado3) / 2
    area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
    print("El triángulo es escaleno.")
    print("Área:", round(area, 2))
