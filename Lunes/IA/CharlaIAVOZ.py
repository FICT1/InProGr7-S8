import win32com.client
import time

engine = win32com.client.Dispatch("SAPI.SpVoice")
voices = engine.GetVoices()
engine.Voice = voices.Item(2)  
engine.Rate = 0
engine.Volume = 100
engine.Speak("Josue es gay")
repeat = 0
repeat_limit = 5
while repeat < repeat_limit:
    engine.Speak("Josue es gay")
