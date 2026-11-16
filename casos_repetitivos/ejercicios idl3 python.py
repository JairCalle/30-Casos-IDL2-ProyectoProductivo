# EJERCICIOS IDL3 - Estructuras repetitivas, arrays, procedimientos y funciones
# Lenguaje: Python 3
# Ejecuta el archivo y selecciona un ejercicio del menú.

import time


def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Ingresa un número mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Ingresa un número menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Debes ingresar un número entero.")


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingresa un número.")


# 1. Suma y promedio de números pares e impares desde 1 hasta N.
def ejercicio_1():
    n = leer_entero("Ingresa N: ", minimo=1)
    pares = [i for i in range(1, n + 1) if i % 2 == 0]
    impares = [i for i in range(1, n + 1) if i % 2 != 0]

    suma_pares = sum(pares)
    suma_impares = sum(impares)
    prom_pares = suma_pares / len(pares) if pares else 0
    prom_impares = suma_impares / len(impares) if impares else 0

    print("\nNÚMEROS PARES:", pares)
    print("Suma de pares:", suma_pares)
    print("Promedio de pares:", prom_pares)
    print("\nNÚMEROS IMPARES:", impares)
    print("Suma de impares:", suma_impares)
    print("Promedio de impares:", prom_impares)


# 2. Clasificar 10 números: pares, impares, positivos, neutros y negativos.
def ejercicio_2():
    pares = impares = positivos = neutros = negativos = 0

    for i in range(1, 11):
        numero = leer_numero(f"Ingresa el número {i}: ")
        if numero == 0:
            neutros += 1
        elif numero > 0:
            positivos += 1
        else:
            negativos += 1

        # La paridad se determina para números enteros.
        if numero.is_integer():
            if int(numero) % 2 == 0:
                pares += 1
            else:
                impares += 1

    print("\nRESULTADOS")
    print("Pares (solo valores enteros):", pares)
    print("Impares (solo valores enteros):", impares)
    print("Positivos:", positivos)
    print("Neutros (ceros):", neutros)
    print("Negativos:", negativos)


# 3. Porcentajes respecto de X.
def ejercicio_3():
    n = leer_entero("¿Cuántos números ingresarás? ", minimo=1)
    x = leer_numero("Ingresa el valor X: ")
    numeros = [leer_numero(f"Número {i + 1}: ") for i in range(n)]

    menores = sum(1 for v in numeros if v < x)
    mayores = sum(1 for v in numeros if v > x)
    iguales = sum(1 for v in numeros if v == x)
    # Se considera el intervalo entre 1 y X, incluyendo sus extremos.
    limite_inferior, limite_superior = sorted((1, x))
    entre_1_y_x = sum(1 for v in numeros if limite_inferior <= v <= limite_superior)
    # "Ninguna condición" se calcula como complemento de menor, mayor e igual a X.
    ninguna = n - menores - mayores - iguales

    print("\nRESULTADOS")
    print(f"Menores que X: {menores / n * 100:.2f}%")
    print(f"Mayores que X: {mayores / n * 100:.2f}%")
    print(f"Iguales a X: {iguales / n * 100:.2f}%")
    print(f"Comprendidos entre 1 y X (incluye extremos): {entre_1_y_x / n * 100:.2f}%")
    print(f"No cumplen ninguna de las tres primeras condiciones: {ninguna / n * 100:.2f}%")


# 4. Máximo y mínimo de una lista.
def ejercicio_4():
    n = leer_entero("Cantidad de números: ", minimo=1)
    numeros = [leer_numero(f"Ingresa el número {i + 1}: ") for i in range(n)]
    print("Lista:", numeros)
    print("Máximo:", max(numeros))
    print("Mínimo:", min(numeros))


# 5. Ahorro acumulado durante 12 meses.
def ejercicio_5():
    ahorro_total = 0
    for mes in range(1, 13):
        deposito = leer_numero(f"Depósito del mes {mes}: S/ ")
        while deposito < 0:
            print("El depósito no puede ser negativo.")
            deposito = leer_numero(f"Depósito del mes {mes}: S/ ")
        ahorro_total += deposito
        print(f"Ahorro acumulado al mes {mes}: S/ {ahorro_total:.2f}")
    print(f"\nAHORRO FINAL DEL AÑO: S/ {ahorro_total:.2f}")


# 6. Cronómetro referencial hh:mm:ss.
def ejercicio_6():
    duracion = leer_entero("¿Cuántos segundos deseas que dure el cronómetro? ", minimo=1)
    print("Cronómetro iniciado. Presiona Ctrl+C para detenerlo antes.")
    try:
        for transcurrido in range(duracion + 1):
            horas = transcurrido // 3600
            minutos = (transcurrido % 3600) // 60
            segundos = transcurrido % 60
            print(f"\r{horas:02d}:{minutos:02d}:{segundos:02d}", end="", flush=True)
            if transcurrido < duracion:
                time.sleep(1)
        print("\nTiempo finalizado.")
    except KeyboardInterrupt:
        print("\nCronómetro detenido.")


# 7. Factoriales de dos números y hasta qué múltiplo coinciden.
def factorial_y_expresion(n):
    resultado = 1
    factores = []
    for i in range(1, n + 1):
        resultado *= i
        factores.append(str(i))
    expresion = " x ".join(factores) if factores else "1"
    return resultado, expresion


def ejercicio_7():
    a = leer_entero("Primer número (0 o mayor): ", minimo=0)
    b = leer_entero("Segundo número (0 o mayor): ", minimo=0)

    fact_a, expr_a = factorial_y_expresion(a)
    fact_b, expr_b = factorial_y_expresion(b)

    print(f"\n{a}! = {expr_a} = {fact_a}")
    print(f"{b}! = {expr_b} = {fact_b}")
    print(f"Los productos comparten los factores desde 1 hasta {min(a, b)}.")
    if a == b:
        print("Ambos factoriales tienen exactamente los mismos factores.")
    else:
        print(f"Coinciden en los múltiplos/factores hasta {min(a, b)}; luego el factorial del número mayor continúa.")


# 8. Registro de asistentes a una fiesta.
def ejercicio_8():
    edades_h = []
    edades_m = []
    todas_edades = []

    while True:
        edad = leer_entero("Edad del asistente: ", minimo=0)
        while True:
            sexo = input("Sexo (H = hombre / M = mujer): ").strip().upper()
            if sexo in ("H", "M"):
                break
            print("Ingresa H o M.")

        todas_edades.append(edad)
        if sexo == "H":
            edades_h.append(edad)
        else:
            edades_m.append(edad)

        continuar = input("¿Deseas registrar a otra persona? (S/N): ").strip().upper()
        if continuar != "S":
            break

    print("\nRESULTADOS")
    print("Total de asistentes:", len(todas_edades))
    print("Hombres:", len(edades_h))
    print("Mujeres:", len(edades_m))
    if edades_h:
        print("Promedio de edad de hombres:", sum(edades_h) / len(edades_h))
    else:
        print("No se registraron hombres.")
    if edades_m:
        print("Promedio de edad de mujeres:", sum(edades_m) / len(edades_m))
    else:
        print("No se registraron mujeres.")
    print("Menor edad:", min(todas_edades))
    print("Mayor edad:", max(todas_edades))


# 9. Producto 100 x 98 x 96 x ... x 2.
def ejercicio_9():
    numeros = list(range(100, 0, -2))
    producto = 1
    for numero in numeros:
        producto *= numero
    print("Array:", numeros)
    print("Producto:", producto)


# 10. Estadísticas de notas de 5 a 20 estudiantes.
def ejercicio_10():
    n = leer_entero("Cantidad de estudiantes (5 a 20): ", minimo=5, maximo=20)
    notas = []

    for i in range(n):
        nota = leer_entero(f"Nota del estudiante {i + 1} (0 a 20): ", minimo=0, maximo=20)
        notas.append(nota)

    mayor = max(notas)
    menor = min(notas)
    aprobados = sum(1 for nota in notas if nota >= 13)
    desaprobados = n - aprobados
    pares = sum(1 for nota in notas if nota % 2 == 0)
    impares = sum(1 for nota in notas if nota % 2 != 0)

    print("\nRESULTADOS DEL SALÓN")
    print("Notas:", notas)
    print("Mayor nota:", mayor)
    print("Menor nota:", menor)
    print("Cantidad que obtuvo la mayor nota:", notas.count(mayor))
    print("Cantidad que obtuvo la menor nota:", notas.count(menor))
    print(f"Promedio del salón: {sum(notas) / n:.2f}")
    print("Notas pares:", pares)
    print("Notas impares:", impares)
    print("Alumnos aprobados (13 a 20):", aprobados)
    print("Alumnos desaprobados (0 a 12):", desaprobados)
    print(f"Porcentaje de aprobados: {aprobados / n * 100:.2f}%")
    print(f"Porcentaje de desaprobados: {desaprobados / n * 100:.2f}%")


def menu():
    ejercicios = {
        "1": ejercicio_1,
        "2": ejercicio_2,
        "3": ejercicio_3,
        "4": ejercicio_4,
        "5": ejercicio_5,
        "6": ejercicio_6,
        "7": ejercicio_7,
        "8": ejercicio_8,
        "9": ejercicio_9,
        "10": ejercicio_10,
    }

    while True:
        print("\n========== MENÚ DE EJERCICIOS ==========")
        for numero in range(1, 11):
            print(f"{numero}. Ejercicio {numero}")
        print("0. Salir")

        opcion = input("Selecciona un ejercicio: ").strip()
        if opcion == "0":
            print("Programa finalizado.")
            break
        if opcion in ejercicios:
            print(f"\n--- EJERCICIO {opcion} ---")
            ejercicios[opcion]()
        else:
            print("Opción no válida. Elige del 0 al 10.")


if __name__ == "__main__":
    menu()
