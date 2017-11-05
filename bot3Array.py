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
                print ("if",s," in ",w)
                if (s == w)  :
                    found = True
        return False

def CheckactionGet (sentence ):
    if(sentence == None):
        print("I did not heard you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in get_key:
            for w in words:
                if (s == w)  :
                    found = True
        return False

def CheckactionDel (sentence ):
    if(sentence == None):
        print("I did not heard you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in del_key:
            if s in words  :
                found = True
        return False


def CheckactionNum (sentence ):
    if(sentence == None):
        print("I did not heard you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in num_key:
            if s in words  :
                found = True
        return False

def CheckactionExist (sentence ):
    if(sentence == None):
        print("I did not head you")
        return False
    else:
        found = False
        words = sentence.split()
        for s in exist_key:
            if s in words  :
                found = True
        return False

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
            print ("Sorry, I am lost. ")
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
        if( CheckactionAdd(text)):
            print ("Say the name of your item to add")
            name = listening()
            myList.append(name)
        if( CheckactionGet(text)):
            myList
        if(CheckactionDel(text)):
            print ("Say the name of the item to delete")
            name = listening()
            myList.remove(name)
        if(CheckactionNum(text)):
            print (" You have: ",len(myList))
        if(CheckactionExist(text)):
            x = name in myList
            if(x): print(name," exist")
            else: print(name," does not exist")
        if(leavingCheck(text)):
            end = 0
        print (" Do you want to continue ? say yes or no")
        text = listening()
        if( Checkword("no", text)):
            end = 0
            print(' Bye ')

            

