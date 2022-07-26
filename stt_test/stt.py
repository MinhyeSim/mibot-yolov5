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
        tts = gTTS(text = "신나는 여행이 될 수 있도록 딱 맞는 음악을 추천해 드릴까요?  ", lang="ko")
        tts.save(f"{self.path}/recommend2.mp3") 

    def mibot_speak(self):       
        return playsound.playsound(f"{self.path}/mibot.mp3") 

    def bye_speak(self):       
        return playsound.playsound(f"{self.path}/bye.mp3") 

    def music_speak(self):       
        return playsound.playsound(f"{self.path}/kobert.mp3") 

    def happy_speak1(self):       
        return playsound.playsound(f"{self.path}/jeju.mp3") 
    
    def happy_speak2(self):       
        return playsound.playsound(f"{self.path}/recommend2.mp3")
    
    def happy_speak3(self):       
        return playsound.playsound(f"{self.path}/play2.mp3") 
    

    
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
                print("다시 말 하세요: " + str(e))
        return said 

    def user_sad(self):
        self.mibot_speak()
           
        while 1:
            self.text = self.get_audio()
            if "대화 종료" in self.text:
                self.bye_speak()
                break
            elif "음악 추천" in self.text:
                self.music_speak()                
            elif "면접" in self.text:
                self.sad_speak1()
            elif "합격" in self.text:
                self.sad_speak2()
            elif "슬퍼" in self.text:
                self.sad_speak3()   

    def user_happy(self):
        self.mibot_speak()
           
        while 1:
            self.text = self.get_audio()
            if "대화 종료" in self.text:
                self.bye_speak()
                break
            elif "음악 추천" in self.text:
                self.music_speak()                
            elif "제주도 여행" in self.text:
                self.happy_speak1()
            elif "기대돼" in self.text:
                self.happy_speak2()
            elif "행복해" in self.text:
                self.happy_speak3()   

                
    
if __name__ == "__main__": 
    #Solution().save_file()
    #Solution().mibot_speak()
    #Solution().bye_speak()
    #Solution().music_speak()
    #Solution().sad_speak1()
    #Solution().sad_speak2()
    #Solution().sad_speak3()
    #Solution().happy_speak1()
    #Solution().happy_speak2()
    #Solution().happy_speak3()
    #Solution().user_sad()
    Solution().user_happy()





