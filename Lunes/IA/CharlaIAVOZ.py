import win32com.client
import time
import os 
os.system('cls' if os.name == 'nt' else 'clear')
#hecho por mi 
engine = win32com.client.Dispatch("SAPI.SpVoice")
voices = engine.GetVoices()
engine.Voice = voices.Item(2)  
engine.Rate = 0
engine.Volume = 100
print("Elige una voz:")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.GetDescription()}")
print ("----------------------")
voice_choice = int(input("Selecciona el número de la voz: "))
engine.Voice = voices.Item(voice_choice)
engine.Rate = 0
engine.Volume = 100
if engine.Rate < -10 or engine.Rate > 10:
    print("La velocidad de voz debe estar entre -10 y 10. Se establecerá en 0.")
    engine.Rate = 0
print ("-----------------------")
rate_choice = int(input("Selecciona la velocidad de voz (0-10): "))
engine.Rate = rate_choice * 10
if engine.Rate < -10 or engine.Rate > 10:
    print("La velocidad de voz debe estar entre -10 y 10. Se establecerá en 0.")
    engine.Rate = 0
print ("-----------------------")
volume_choice = int(input("Selecciona el volumen de voz (0-100): "))
if volume_choice < 0 or volume_choice > 100:
    print("El volumen debe estar entre 0 y 100. Se establecerá en 100.")
    volume_choice = 100
engine.Rate = rate_choice
engine.Volume = volume_choice
print ("****************************************")
time.sleep(2)
print("Escribe el texto que deseas que lea la voz")
text_choice = input("Escribe el texto: ")
engine.Speak(text_choice)
time.sleep(2)
print ("***Deseas repetir el texto? (s/n)***")
repeat_choice = input("Escribe 's' para repetir o 'n' para salir\n-> ")
if repeat_choice.lower() == 's':
    text_choice = input("Escribe el texto nuevamente\n-> ")
    engine.Speak(text_choice)
elif repeat_choice.lower() == 'n':
    print("Saliendo...")
else:
    print("Opción no válida. Saliendo...")
time.sleep(2)
print ("Fin del programa")



