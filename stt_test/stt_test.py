#import speech_recognition as sr
from gtts import gTTS
# import os
# import time
from playsound import playsound



text = "화가 난다."
tts = gTTS(text = text, lang="ko")
tts.save(r"stt_test\voice.mp3")
playsound(r"stt_test\voice.mp3")

'''
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
            audio = r.listen(source)
            said = " "
            
            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception: " + str(e))
    return said

speak("안녕하세요, 당신의 미봇입니다.")
text = get_audio()
if "안녕" in text:
    speak("좋은 날이에요.")
elif "심심해" in text:
    speak("정신차려요. 이 각박한 세상에서")
'''