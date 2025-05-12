#for 

import win32com.client
engine = win32com.client.Dispatch("SAPI.SpVoice")
voices = engine.GetVoices()
for i in range (1,4):              #BUCLE EXTERNO
    for j in range (1,4):          #BUCLE INTERNO
        print (f"{i}, {j}")
        engine.Speak(f"{i}, {j}")
    print ("---------------------")

    