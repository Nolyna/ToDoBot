#!/usr/bin/env python

import speech_recognition as sr
import sqlite3
import sys
import random

#connect to database
conn = sqlite3.connect('test1.db')

################## functions            

########### BOT

def listening():
    with sr.Microphone() as source:
            audio = r.listen(source)
            print ('Done!')

    try:
        text = r.recognize_google(audio)
        print('I heard: ' + text)
        return text 
        
                
    except Exception as e:
        print (e)
            
def Checkword( word, sentence ):
    if(sentence == None):
        print("I did not heard you")
        return False
    else:
        words = sentence.split()
        if word in words: 
           return True
        else:
            return False

def CheckactionAdd (sentence ):
    if(sentence == None):
        print("I did not heard you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in build_key:
            for w in words:
                s = s.strip()
                w = w.strip()
                #print ("if",s," in ",w)
                if (s == w)  :
                    found = True
        return found

def CheckactionGet (sentence ):
    if(sentence == None):
        print("I did not heard you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in get_key:
            for w in words:
                if (s.strip() == w.strip())  :
                    found = True
        return found

def CheckactionDel (sentence ):
    if(sentence == None):
        print("I did not heard you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in del_key:
            s = s.strip()
            if s in words  :
                found = True
        return found


def CheckactionNum (sentence ):
    if(sentence == None):
        print("I did not heard you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in num_key:
            s = s.strip()
            if s in words  :
                found = True
        return found

def CheckactionExist (sentence ):
    if(sentence == None):
        print("I did not head you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in exist_key:
            s = s.strip()
            if s in words  :
                found = True
        return found

# Sentences by the user
greeting_key = ("hello", "hi", "greetings", "sup", "what's up")
leaving_key = ("bye", "end", "finish", "over", "leaving")
build_key = ("create","new","add","more")
get_key = ("get","show","give")
del_key = ("delete","remove")
num_key = ("how many","many", "much", "how", "number")
exist_key = ("into","exist", "inside")

# Bot response
greeting_response = ["Hi there", "hey", "How are you ? I'm good", "hello you! "]
leaving_response = ["Bye", "See you", "Come back", " Don't leave me!!! "]

def greetingCheck(sentence):
    if(sentence == None):return False
    else:
         for word in greeting_key:
            #y = sentence.split()
            if word in  sentence:
                x = random.choice(greeting_response)
                print (x)
                return True
            else:
                print ("Sorry, I did not understand that. But Hello ")
                return False
    

def leavingCheck(sentence):
    for word in leaving_key:
        if word in sentence:
            x = random.choice(leaving_response)
            print (x)
            return True
        else:
            #print ("Sorry, I am lost. ")
            return False
    

############################# Main
r = sr.Recognizer()
end = 1
myList = []
lang = 'en'

#while True:
print ('listening')
text = listening()
greetingCheck(text)
        
while (end == 1):

        print ("What do you want to do with your list? ( add, show, remove,how much, exist)")
        text = listening()
        t = text.split()
        size = len(t)
        if(size == 1):
            if( CheckactionAdd(text)):
                print ("Say the name of your item to add")
                name = listening()
                myList.append(name)
                print ("Added. ", myList)
            elif( CheckactionGet(text)):
                myList
            elif(CheckactionDel(text)):
                print ("Say the name of the item to delete")
                name = listening()
                myList.remove(name)
                print ("Deleted")
            elif(CheckactionNum(text)):
                print (" You have: ",len(myList))
            elif(CheckactionExist(text)):
                x = name in myList
                if(x): print(name," exist")
                else: print(name," does not exist")
            elif(leavingCheck(text)):
                end = 0
        else:
            v = ""
            for i in t[1:]:
                v = v+i
            if( CheckactionAdd(t[0])):
                myList.append(v)
                print ("Added",  myList)
            elif(CheckactionDel(t[0])):
                myList.remove(v)
                print ("Deleted")
            elif(CheckactionExist(t[0])):
                x = v in myList
                if(x): print(name," exist")
                else: print(name," does not exist")
            
        print (" Do you want to continue ? say yes or no")
        text = listening()
        if( Checkword("no", text)):
            end = 0
            print(' Bye ')

            

