import win32com.client
#ESTO TE DICE CUALES VOCES TIENES EN EL ORDENADOR
#ESTO TE DICE CUALES VOCES TIENES EN EL ORDENADOR
engine = win32com.client.Dispatch("SAPI.SpVoice")
voices = engine.GetVoices()

for i, voice in enumerate(voices):
    print(f"{i}: {voice.GetDescription()}")