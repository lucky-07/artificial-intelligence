#run this file only on jupiter

#install pyttsx3
#pip install pyttsx3


#install wikipedia
#pip install wikipedia

#CODE
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def lan():
    
    
    print("For English enter e or E , For Hindi enter h or H")
    speak("For English enter e or E , For Hindi enter h or H")
    a = input()
    return a

def greet():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <23:
        print("BOT: HELLO",end=" ")
        speak("HELLO")

def greet1():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <23:
        print("BOT: Namaste",end=" ")
        speak("Namaste")
        
        
   
  
def issue():
    
    
    print("BOT :Hello i am stress buster bot")
    speak("BOT :Hello i am stress buster bot")
    print("BOT: i am here to help to solve your problem")
    speak(" i am here to help to solve your problem")
    
    print("please make the sentences related to given keywords")
    speak("please make the sentences related to given keywords")
    print("As i am stress buster bot")
    speak("As i am stress buster bot")
    
    print("so enter the sentences with givwn keywords like pain, sad, stress etc")
    speak("so enter the sentences with givwn keywords like pain, sad, stress etc")
    print("now tell me your problem")
    speak("now tell me your problem")

   
    
    
def sad():

    print("Why are you sad?")
    speak("Why are you sad?")
    print("Tell me in brief")
    speak("Tell me in brief")
    
    print("like you are sad because of love,loneliness,breakup,missing someone or something etc")
    speak("like you are sad because of love,loneliness,breakup,missing someone or something etc")
    print("you can share with me anything")
    speak("you can share with me anything")
    
    print("i will try to solve your problem")
    speak("i will try to solve your problem")
    
    a = input().lower()
    if 'loves' in a:
        print("Why you think like that?")
        speak("Why you think like that")
        print("sometimes a person thing like that according to the situation")
        speak("sometimes a person thing like that according to the situation")
        print("everything gonna be fine after sometime")
        speak("everything gonna be fine after sometime")
        
        print("so don't think like that")
        speak("so don't think like that")
        print("are you okay now : yes or no")
        speak("are you okay now : yes or no")
        d = input().lower()
        
        if 'yes' in d:
            print("thats great")
            speak("thats great")
        elif 'no' in d:
            print("don't worry everything gonna be fine")
            speak("don't worry everything gonna be fine")
        
    
    elif 'single' in a or 'lonely' in a:
        print("No you are not single")
        speak("No you are not single")
        print("i am here with you haha")
        speak("i am here with you haha")
        print("by the way...are you married: yes or no")
        speak("by the way...are you married: yes or no")
        d=input().lower()
        
        
        if "yes" in d:
            print("cool then why you feel lonely or single")
            speak("cool then why you feel lonely or single")
            
        elif "no" in d:
            print("do not worry")
            speak("do not worry")
            print("soon you will find your life partner ")
            speak("soon you will find your life partner")
            

    elif 'breakup' in a:
        print("oh wow thats great news")
        speak("oh wow thats great news")
        print("thats not a problem")
        speak("thats not a problem")
        print("now you can make new life partner")
        speak("now you can make new life partner")
        print("so be happy and explore the world")
        speak("so be happy and explore the world")
        print("i can give you an platform where you can find your new partner")
        speak("i can give you an platform where you can find your new partner")
        print("you want it : yes or no")
        speak("you want it : yes or no")
       
    
        d=input().lower()
       
        if 'yes' in d:
            webbrowser.open("https://twitter.com/login?lang=en")
        elif 'no' in d:
            print("okay")
            speak("okay")
    
    
    elif 'missing' in a:
        print("I will cover the memories of missing person")
        speak("I will cover the memories of missing person")
        print("you can talk with me if you missing someone")
        speak("you can talk with me if you missing someone")
        print("BE HAPPY")
        speak("BE HAPPY")
        
        

        
def pain():
    
    print("Ok you are suffering with pain")
    speak("Ok you are suffering with pain")
    print("what kind of pain you suffer from")
    speak("what kind of pain you suffer from")
    
    print("like back pain,headache,body pain, pain in eye or ear,pain in hand, leg pain etc")
    speak("like back pain,headache,body pain, pain in eye or ear,pain in hand, leg pain etc")
    print("I will try to give better solution")
    speak("I will try to give better solution")
    print("now tell me")
    
    speak("now tell me")
    
    a = input().lower()
    if 'body' in a:
        print("okay tell me that")
        speak("okay tell me that")
        print("you have minor pain or major pain")
        speak("you have minor pain or major pain")
        d=input().lower()
        if 'minor' in d:
            print("you should take rest for a while")
            speak("you should take rest for a while")
        elif 'major' in d:
            print("you should consult with doctor")
            speak("you should consult with doctor")
            print("otherwise you should take any painkiller")
            speak("otherwise you should take any painkiller")
            print("i reccommend you paracetamol")
            speak("i reccommend you paracetamol")
    
    elif 'head' in a:
        print("okay tell me that")
        speak("okay tell me that")
        print("you have minor pain or major pain")
        speak("you have minor pain or major pain")
        
        d=input().lower()
        
        if 'minor' in d:
            print("you should take rest for a while")
            speak("you should take rest for a while")
        elif 'major' in d:
            print("you should consult with doctor")
            speak("you should consult with doctor")
            print("otherwise you should take any painkiller")
            speak("otherwise you should take any painkiller")
            print("i reccommend you paracetamol")
            speak("i reccommend you paracetamol")
    
       
    elif 'leg' in a:
        
        print("okay tell me that")
        speak("okay tell me that")
        print("you have minor pain or major pain")
        speak("you have minor pain or major pain")
        
        d=input().lower()
        
        if 'minor' in d:
            print("you should take rest for a while")
            speak("you should take rest for a while")
        elif 'major' in d:
            print("you should consult with doctor")
            speak("you should consult with doctor")
            print("otherwise you should take any painkiller")
            speak("otherwise you should take any painkiller")
            print("i reccommend you paracetamol")
            speak("i reccommend you paracetamol")
        
    elif 'hand' in a:
        
        print("okay tell me that")
        speak("okay tell me that")
        print("you have minor pain or major pain")
        speak("you have minor pain or major pain")
        
        d=input().lower()
        
        if 'minor' in d:
            print("you should take rest for a while")
            speak("you should take rest for a while")
        elif 'major' in d:
            print("you should consult with doctor")
            speak("you should consult with doctor")
            print("otherwise you should take any painkiller")
            speak("otherwise you should take any painkiller")
            print("i reccommend you paracetamol")
            speak("i reccommend you paracetamol")
    
    elif 'shoulder' in a:
        
        print("okay tell me that")
        speak("okay tell me that")
        print("you have minor pain or major pain")
        speak("you have minor pain or major pain")
        d=input().lower()
        if 'minor' in d:
            print("you should take rest for a while")
            speak("you should take rest for a while")
        elif 'major' in d:
            print("you should consult with doctor")
            speak("you should consult with doctor")
            print("otherwise you should take any painkiller")
            speak("otherwise you should take any painkiller")
            print("i reccommend you paracetamol")
            speak("i reccommend you paracetamol")
            
            
    elif 'eye' in a:
        
        print("okay tell me that")
        speak("okay tell me that")
        print("you have minor pain or major pain")
        speak("you have minor pain or major pain")
        
        d=input().lower()
        
        if 'minor' in d:
            print("you should take rest for a while")
            speak("you should take rest for a while")
        elif 'major' in d:
            print("you should consult with doctor")
            speak("you should consult with doctor")
            print("otherwise you should take any eye drop")
            speak("otherwise you should take any eye drop")
            
    elif 'ear' in a:
        
        print("okay tell me that")
        speak("okay tell me that")
        print("you have minor pain or major pain")
        speak("you have minor pain or major pain")
        
        d=input().lower()
        
        if 'minor' in d:
            print("you should take rest for a while")
            speak("you should take rest for a while")
        elif 'major' in d:
            print("you should consult with doctor")
            speak("you should consult with doctor")
            print("otherwise you should take any ear drop")
            speak("otherwise you should take any ear drop")
            
    
def stress():
    
    print("everyone have so many differnt types of stress")
    speak("everyone have so many differnt types of stress")
    print("now you tell what kind of stress you have")
    speak("now you tell what kind of stress you have")
    print("like exam stress, future stress, result stress,good or bad times etc")
    speak("like exam stress, future stress, result stress,good or bad times etc")
    print("I will try to give proper guidance about it")
    speak("I will try to give proper guidance about it")
    
    a = input().lower()
    
    if 'exam' in a or 'paper' in a:
        
        print("oh thats a genuine problem")
        speak("oh thats a genuine problem")
        print("okay tell me that are you a hardworking guy : yes or no")
        speak("okay tell me that are you a hardworking guy : yes or no")
        d= input().lower()
        if 'yes' in d:
            print("then there should not be any problem at all")
            speak("then there should not be any problem at all")
            print("with hardwork you should do good management of time")
            speak("with hardwork you should do good management of time")
            print("then you will surely succeed in your life")
            speak("then you will surely succeed in your life")
        elif 'no' in d:
            print("you should do hardwork and be puntual with time")
            speak("you should do hardwork and be puntual with time")
        
    
    elif 'future' in a or 'carrier' in a:
        
        print("I Can understand your problem")
        speak("I Can understand your problem")
        print("if you are doing proper harwork then you will surely achieve your goals")
        speak("if you are doing proper harwork then you will surely achieve your goals")
        print("so do not worry about the what going to happen in future")
        speak("so do not worry about the what going to happen in future")

    elif 'result' in a or 'outcomes' in a:
        print("i get your problem")
        speak("i get your problem")
        print("if you are giving your best then do not worry about result or outcomes")
        speak("if you are giving your best then do not worry about result or outcomes")
        print("everything will be fine")
        speak("everything will be fine")
    
    elif 'good' in a or 'bad' in a:
        print("good or bad are only working according the time")
        speak("good or bad are only working according the time")
        print("everyone have phase when they have good or bad")
        speak("everyone have phase when they have good or bad")
        print("so think so much about the it")
        speak("so think so much about the it")
        

        

# MAIN
if __name__  == "__main__":
    
    a = lan()
    b='x'
    
    if a=='e' or a=='E':
        greet()
        c=input('greeting: ')
        while b!='q':
            issue()
            d = input().lower()
        
            
            if 'sad' in d or 'happy' in d:
                sad()
                b=input("If you want to quit enter q otherwise enter any other key")
        
            elif 'pain' in d:
                pain()
                b=input("If you want to quit enter q otherwise enter any other key")

            
            elif 'stress' in d or 'tension' in d:
                stress()
                b=input("If you want to quit enter q otherwise enter any other key")

    
    elif a=='h' or a=='H':
        greet1()
        c=input('greeting: ')
        while b!='q':
            issue()
            d = input().lower()
        
            
            if 'sad' in d:
                sad()
                b=input("If you want to quit enter q otherwise enter any other key")
        
            elif 'pain' in d:
                pain()
                b=input("If you want to quit enter q otherwise enter any other key")

            
            elif 'stress' in d:
                stress()
                b=input("If you want to quit enter q otherwise enter any other key")
    else:
        print("please select a valid input")
        speak("please select a valid input")

    







