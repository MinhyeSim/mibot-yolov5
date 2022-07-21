from gtts import gTTS #gtts 라이브러리에서 gTTS만 사용 하겠다.
from playsound import playsound

class Solution:

    def __init__(self):
    
        self.text = "안녕하세요 당신의 미봇이에요"
        self.tts = gTTS(text = self.text, lang="ko")
        self.tts.save(r"C:\Users\bitcamp\mibot\mibot-yolov5\yolov5\tts_test\hi.mp3")
    
    def main(self):
        return playsound(r"C:\Users\bitcamp\mibot\mibot-yolov5\yolov5\tts_test\hi.mp3")

if __name__ == "__main__": 
    Solution().main()
