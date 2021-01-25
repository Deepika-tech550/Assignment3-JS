import pyttsx3
def fun(msg):
    friend=pyttsx3.init()
    friend.say(msg)
    friend.runAndWait()
    
    friend.stop()
    print("Successfulluy Speaked!!!!!")
text=input("Enter The Text To Speak")    
fun(text)
