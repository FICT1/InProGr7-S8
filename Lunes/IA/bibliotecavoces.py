import win32com.client

engine = win32com.client.Dispatch("SAPI.SpVoice")
voices = engine.GetVoices()

for i, voice in enumerate(voices):
    print(f"{i}: {voice.GetDescription()}")