import speech_recognition as sr
from gtts import gTTS
import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT) # light
GPIO.setup(3, GPIO.OUT) # fan

GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)

# Initial Greeting (Hindi + English)
welcome_text = "à¤¨à¤®à¤¸à¥à¤¤à¥‡ à¤®à¥‡à¤°à¤¾ à¤¨à¤¾à¤® à¤®à¤¾à¤¨à¤µà¥€ à¤¹à¥ˆ, à¤®à¥ˆà¤‚ à¤†à¤ªà¤•à¥€ à¤•à¥à¤¯à¤¾ à¤¸à¤¹à¤¾à¤¯à¤¤à¤¾ à¤•à¤° à¤¸à¤•à¤¤à¥€ à¤¹à¥‚à¤. Hello, my name is Manvi, how can I help you?"
myobj = gTTS(text=welcome_text, lang='hi', slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")

try:
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak now...")
            audio = r.listen(source)

        try:
            data = r.recognize_google(audio, language='hi')
        except:
            data = "Could not understand anything"
        try:
            
            data1 = r.recognize_google(audio, language='en-in')
        except:
            data1 = "Could not understand anything"

        print("You said:", data)

        ############### HINDI VOICE COMMANDS ###############

        if data in ['à¤²à¤¾à¤‡à¤Ÿ à¤‘à¤¨ à¤•à¤°à¥‹', 'à¤²à¤¾à¤‡à¤Ÿ à¤‘à¤¨ à¤•à¤°', 'à¤²à¤¾à¤‡à¤Ÿ à¤šà¤¾à¤²à¥‚ à¤•à¤°', 'à¤²à¤¾à¤‡à¤Ÿ à¤šà¤¾à¤²à¥‚ à¤•à¤°à¥‹']:
            print("Light ON")
            GPIO.output(2, GPIO.LOW)
            myobj = gTTS(text='à¤®à¥ˆà¤‚à¤¨à¥‡ à¤²à¤¾à¤‡à¤Ÿ à¤‘à¤¨ à¤•à¤° à¤¦à¤¿à¤¯à¤¾', lang='hi')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data in ['à¤²à¤¾à¤‡à¤Ÿ à¤‘à¤« à¤•à¤°à¥‹', 'à¤²à¤¾à¤‡à¤Ÿ à¤‘à¤« à¤•à¤°', 'à¤²à¤¾à¤‡à¤Ÿ à¤¬à¤‚à¤¦ à¤•à¤°à¥‹', 'à¤²à¤¾à¤‡à¤Ÿ à¤¬à¤‚à¤¦ à¤•à¤°']:
            print("Light OFF")
            GPIO.output(2, GPIO.HIGH)
            myobj = gTTS(text='à¤®à¥ˆà¤‚à¤¨à¥‡ à¤²à¤¾à¤‡à¤Ÿ à¤‘à¤« à¤•à¤° à¤¦à¤¿à¤¯à¤¾', lang='hi')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data in ['à¤ªà¤‚à¤–à¤¾ à¤‘à¤¨ à¤•à¤°à¥‹', 'à¤ªà¤‚à¤–à¤¾ à¤‘à¤¨ à¤•à¤°', 'à¤ªà¤‚à¤–à¤¾ à¤šà¤¾à¤²à¥‚ à¤•à¤°', 'à¤ªà¤‚à¤–à¤¾ à¤šà¤¾à¤²à¥‚ à¤•à¤°à¥‹']:
            print("Fan ON")
            GPIO.output(3, GPIO.LOW)
            myobj = gTTS(text='à¤®à¥ˆà¤‚à¤¨à¥‡ à¤ªà¤‚à¤–à¤¾ à¤‘à¤¨ à¤•à¤° à¤¦à¤¿à¤¯à¤¾', lang='hi')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data in ['à¤ªà¤‚à¤–à¤¾ à¤‘à¤« à¤•à¤°à¥‹', 'à¤ªà¤‚à¤–à¤¾ à¤‘à¤« à¤•à¤°', 'à¤ªà¤‚à¤–à¤¾ à¤¬à¤‚à¤¦ à¤•à¤°à¥‹', 'à¤ªà¤‚à¤–à¤¾ à¤¬à¤‚à¤¦ à¤•à¤°']:
            print("Fan OFF")
            GPIO.output(3, GPIO.HIGH)
            myobj = gTTS(text='à¤®à¥ˆà¤‚à¤¨à¥‡ à¤ªà¤‚à¤–à¤¾ à¤‘à¤« à¤•à¤° à¤¦à¤¿à¤¯à¤¾', lang='hi')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data in ['à¤²à¤¾à¤‡à¤Ÿ à¤ªà¤‚à¤–à¤¾ à¤‘à¤¨ à¤•à¤°à¥‹', 'à¤²à¤¾à¤‡à¤Ÿ à¤ªà¤‚à¤–à¤¾ à¤šà¤¾à¤²à¥‚ à¤•à¤°à¥‹', 'à¤²à¤¾à¤‡à¤Ÿ à¤ªà¤‚à¤–à¤¾ à¤šà¤¾à¤²à¥‚ à¤•à¤°', 'à¤²à¤¾à¤‡à¤Ÿ à¤ªà¤‚à¤–à¤¾ à¤‘à¤¨ à¤•à¤°']:
            print("Light + Fan ON")
            GPIO.output(2, GPIO.LOW)
            GPIO.output(3, GPIO.LOW)
            myobj = gTTS(text='à¤®à¥ˆà¤‚à¤¨à¥‡ à¤²à¤¾à¤‡à¤Ÿ à¤”à¤° à¤ªà¤‚à¤–à¤¾ à¤‘à¤¨ à¤•à¤° à¤¦à¤¿à¤¯à¤¾', lang='hi')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data in ['à¤²à¤¾à¤‡à¤Ÿ à¤ªà¤‚à¤–à¤¾ à¤‘à¤« à¤•à¤°à¥‹', 'à¤²à¤¾à¤‡à¤Ÿ à¤ªà¤‚à¤–à¤¾ à¤¬à¤‚à¤¦ à¤•à¤°à¥‹', 'à¤²à¤¾à¤‡à¤Ÿ à¤ªà¤‚à¤–à¤¾ à¤¬à¤‚à¤¦ à¤•à¤°', 'à¤²à¤¾à¤‡à¤Ÿ à¤ªà¤‚à¤–à¤¾ à¤‘à¤« à¤•à¤°']:
            print("Light + Fan OFF")
            GPIO.output(2, GPIO.HIGH)
            GPIO.output(3, GPIO.HIGH)
            myobj = gTTS(text='à¤®à¥ˆà¤‚à¤¨à¥‡ à¤²à¤¾à¤‡à¤Ÿ à¤”à¤° à¤ªà¤‚à¤–à¤¾ à¤‘à¤« à¤•à¤° à¤¦à¤¿à¤¯à¤¾', lang='hi')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        ############### ENGLISH VOICE COMMANDS ###############

        if data1 in ['Manvi can you turn on light', 'turn on light Manvi', 'turn on light']:
            print("Light ON")
            GPIO.output(2, GPIO.LOW)
            myobj = gTTS(text='I turned on the light', lang='en-in')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data1 in ['Manvi can you turn off light', 'turn off light Manvi', 'turn off light']:
            print("Light OFF")
            GPIO.output(2, GPIO.HIGH)
            myobj = gTTS(text='I turned off the light', lang='en-in')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data1 in ['Manvi can you turn on fan', 'turn on fan Manvi', 'turn on fan']:
            print("Fan ON")
            GPIO.output(3, GPIO.LOW)
            myobj = gTTS(text='I turned on the fan', lang='en-in')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data1 in ['Manvi can you turn off fan', 'turn off fan Manvi', 'turn off fan']:
            print("Fan OFF")
            GPIO.output(3, GPIO.HIGH)
            myobj = gTTS(text='I turned off the fan', lang='en-in')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data1 in ['Manvi can you turn on both light and fan', 'turn on light and fan Manvi', 'turn on light and fan']:
            print("Lights + Fan ON")
            GPIO.output(2, GPIO.LOW)
            GPIO.output(3, GPIO.LOW)
            myobj = gTTS(text='I turned on the light and fan', lang='en-in')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")

        if data1 in ['Manvi can you turn off both light and fan', 'turn off light and fan Manvi', 'turn off light and fan']:
            print("Lights + Fan OFF")
            GPIO.output(2, GPIO.HIGH)
            GPIO.output(3, GPIO.HIGH)
            myobj = gTTS(text='I turned off the light and fan', lang='en-in')
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")
        else:
            continue

finally:
    GPIO.cleanup()
