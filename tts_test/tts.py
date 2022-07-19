from gtts import gTTS #gtts 라이브러리에서 gTTS만 사용 하겠다.
from playsound import playsound

text = "안녕하세요. 저는 당신의 미봇이에요."

tts = gTTS(text = text, lang="ko")
tts.save(r"nlp\hi.mp3")

playsound(r"nlp\hi.mp3")

# 22.07.20 미션 : oop로 전환하기 => 추후 장고로 업로드할것이다.