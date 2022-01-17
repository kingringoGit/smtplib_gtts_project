# text to speech
from gtts import gTTS
import os
text="welcome to rayyan classes"
language='en'
obj=gTTS(text=text,lang=language,slow=False)
obj.save('welcome.mp3')
os.system('welcome.mp3')

