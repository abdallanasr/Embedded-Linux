import playsound
import speech_recognition as sr
import os
from gtts import gTTS
import webbrowser

class voice_assistant:
    recognizer = sr.Recognizer()
    def record_audio(self):
        with sr.Microphone() as source:
            print("Listening....")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio

    def recognize_speech(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language="ar-EG")
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Sorry, there was an error processing your request.")
        return " "

    def speak(self, audios):
        tts = gTTS(text=audios, lang='ar', slow=False)
        audioF = 'audio.mp3'
        tts.save(audioF)
        playsound.playsound(audioF)
        print(audios)
        os.remove(audioF)

    def search_words_in_string(self,word_list, text):
        found_words = [word for word in word_list if word in text]
        return len(found_words) != 0

    def Respond(self,voice_data):
        if self.search_words_in_string(["اسمي", "اسم", "الاسم"], voice_data):
            self.speak(" صباح الخير عبدالله")
        elif self.search_words_in_string(["كود", "الكود", "في اس"], voice_data):
            print("done")
            webbrowser.open("https://www.youtube.com/", new=2) 
