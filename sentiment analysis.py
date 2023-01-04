
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('clearing background noise...')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('waiting for your message....')
    try: 
        recordedaudio=recognizer.listen(source)
        print('Done recording...')
    except Exception as ex:
        print(ex)
    
try:
    print('Printing the message...')
    text=recognizer.recognize_google(recordedaudio,language='en-US')
    print('Your message:{}'.format(text))
except Exception as ex:
    print(ex)
    
#sentiment analysis

sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()
for i in sentence:
    v=analyser.polarity_scores(i)
    print(v)