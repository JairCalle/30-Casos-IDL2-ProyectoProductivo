# Caso 8: Ordenar tres números

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Se repite el ingreso si hay números iguales
while num1 == num2 or num1 == num3 or num2 == num3:
    print("Los tres números deben ser diferentes.")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

orden = input("¿Cómo desea ordenarlos? (A = ascendente, D = descendente): ").lower()

# Ordenamos de menor a mayor usando comparaciones
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

if orden == "a":
    print("Orden ascendente:", num1, num2, num3)
elif orden == "d":
    print("Orden descendente:", num3, num2, num1)
else:
    print("Opción no válida. Escriba A o D.")
