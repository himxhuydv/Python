import pyttsx3
import time 
engine=pyttsx3.init()
engine.setProperty('rate',100)
engine.say("hi sir welcome back good to see you again")
engine.runAndWait()
time.sleep(0.5)
engine.say("would you like to have a coffee")
engine.runAndWait()