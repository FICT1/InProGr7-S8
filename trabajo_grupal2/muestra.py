print ("*Promedio de calificaciones*")
import os
import time
os.system("cls || clear")
suma = 0
contador = 0
while True:
    calificacion = float(input("Introduce una calificación (-1 para terminar)\n-> "))
    if calificacion == -1:
        break
    suma += calificacion
    contador += 1
    time.sleep(0.2)
    os.system("cls || clear")
if contador > 0:
    promedio = suma / contador
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
    print(f"Total de calificaciones ingresadas: {contador}")
else:
    print("No se ingresaron calificaciones válidas.")