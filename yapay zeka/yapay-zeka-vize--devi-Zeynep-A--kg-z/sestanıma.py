import speech_recognition as sr
r= sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data=r.record(source, duration=10)
    print("ses tanımlanıyor...")
    text=r.recognize_google(data,language='tr', show_all=True)
    print(text)