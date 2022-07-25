from email.mime import audio
import speech_recognition as sr
from gtts import gTTS
import playsound
from yaml import safe_dump_all

class Solution:

    def __init__(self) :
        #self.text = "말씀하세요"
        #self.tts = gTTS(text = self.text, lang="ko")
        #self.tts.save(r"C:/Users/bitcamp/mibot/mibot-yolov5/yolov5/stt_test\voice.mp3")
        #self.path = "C:/Users/bitcamp/mibot/mibot-yolov5/yolov5/stt_test"
        self.path = "C:/Users/bitcamp/mibot/mibot-yolov5/yolov5/stt_test"
    
    def save_file(self):
        tts = gTTS(text = "저는 미봇이에요, 당신의 이야기를 들려주세요", lang="ko")
        tts.save(f"{self.path}/mibot.mp3")

    def speak(self):       
        return playsound.playsound(f"{self.path}/mibot.mp3") #저는 미봇이에요, 당신의 이야기를 들려주세요

    def speak2(self):       
        return playsound.playsound(f"{self.path}/rest.mp3") #너무 힘들 때는 잠깐의 휴식이 도움 돼요

    def speak3(self):       
        return playsound.playsound(f"{self.path}/music.mp3") #음악을 듣는 건 어떠세요? 기분에 맞는 음악을 추천해 드릴게요.

    def speak4(self):       
        return playsound.playsound(f"{self.path}/kobert.mp3") # 현재 기분은 어떤 상태인가요?
    
    def speak5(self):       
        return playsound.playsound(f"{self.path}/depressed.mp3") # 우울하시군요, 비투비의 괜찮아요를 들려 드릴게요
    
    def speak6(self):       
        return playsound.playsound(f"{self.path}/bye.mp3") # 당신은 충분히 잘하고 있어요. 남은 하루도 행복하게 보내길 바래요
    

    
    ##
    def get_audio(self):
        r = sr.Recognizer() #음성 인식
        with sr.Microphone() as source: #마이크로폰을 소스로 받아들여 
            audio = r.listen(source) # 오디오로 들어간 뒤
            said = "" # 말하기 -> 한국말로 음성 인식 되게 하기 
                 
            try:
                said = r.recognize_google(audio, language='ko-KR')
                print(said)
            except Exception as e:
                print("Exception: " + str(e))
        return said 

    def stt(self):
        self.speak()
           
        while 1:
            self.text = self.get_audio()
            if "스트레스" in self.text:
                self.speak2()
            elif "휴식" in self.text:
                self.speak3()                
            elif "음악" in self.text:
                self.speak4()
            elif "우울해" in self.text:
                self.speak5()
            elif "종료" in self.text:
                self.speak6()   
                break
    
if __name__ == "__main__": 
    #Solution().save_file()
    #Solution().speak()
    #Solution().speak2()
    #Solution().speak3()
    #Solution().speak4()
    #Solution().speak5()
    #Solution().speak6()
    Solution().stt()




