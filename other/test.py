import io

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'zh')

f=open("/home/tianbo/pythonApp/a.txt",'r')
line=f.readline()

engine.say(line)
print(line)