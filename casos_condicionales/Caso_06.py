# Caso 6: Hora después de N segundos

hora = int(input("Ingrese la hora (0 a 23): "))
minuto = int(input("Ingrese los minutos (0 a 59): "))
segundo = int(input("Ingrese los segundos (0 a 59): "))
n = int(input("¿Cuántos segundos desea agregar? "))

if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59 or n < 0:
    print("Ingrese una hora y una cantidad de segundos válidas.")
else:
    # Pasamos todo a segundos y sumamos el tiempo indicado
    total_segundos = hora * 3600 + minuto * 60 + segundo + n
    total_segundos = total_segundos % 86400  # La hora vuelve a 00:00:00 después de un día

    nueva_hora = total_segundos // 3600
    nuevo_minuto = (total_segundos % 3600) // 60
    nuevo_segundo = total_segundos % 60

    print("La nueva hora es: {:02d}:{:02d}:{:02d}".format(nueva_hora, nuevo_minuto, nuevo_segundo))
