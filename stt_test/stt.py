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
        tts = gTTS(text = "슬픈 기분을 위해 비투비의 괜찮아요를 들려 드릴게요", lang="ko")
        tts.save(f"{self.path}/play.mp3") 

    def mibot_speak(self):       
        return playsound.playsound(f"{self.path}/mibot.mp3") 

    def bye_speak(self):       
        return playsound.playsound(f"{self.path}/bye.mp3") 

    def music_speak(self):       
        return playsound.playsound(f"{self.path}/kobert.mp3") 

    def sad_speak1(self):       
        return playsound.playsound(f"{self.path}/cheerup.mp3") 
    
    def sad_speak2(self):       
        return playsound.playsound(f"{self.path}/recommend.mp3")
    
    def sad_speak3(self):       
        return playsound.playsound(f"{self.path}/play.mp3") 
    

    
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
            elif "음악 추천" in self.text:
                self.music_speak()                
            elif "면접" in self.text:
                self.sad_speak1()
            elif "합격" in self.text:
                self.sad_speak2()
            elif "슬퍼" in self.text:
                self.sad_speak3()   
                break
    
if __name__ == "__main__": 
    Solution().save_file()
    #Solution().mibot_speak()
    #Solution().bye_speak()
    #Solution().music_speak()
    #Solution().sad_speak1()
    #Solution().sad_speak2()
    #Solution().sad_speak3()
    Solution().user_sad()




