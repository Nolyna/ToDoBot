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
        print('Did you said:\n' + text)
        return text 
        
                
    except Exception as e:
        print (e)
            
def Checkword( word, sentence ):
    if word in sentence: 
       return True
    else:
        return False

def CheckactionAdd (sentence ):
        if sentence in build_key :
            return True
        else:
           
            return False

def CheckactionGet (sentence ):
        if sentence in get_key :
            return True
        else:
                        return False

def CheckactionDel (sentence ):
        if sentence in del_key :
            return True
        else:
            
            return False

# Sentences by the user
greeting_key = ("hello", "hi", "greetings", "sup", "what's up")
leaving_key = ("bye", "end", "finish", "over", "leaving")
build_key = ("create","new","add","more")
get_key = ("get","show","give")
del_key = ("delete","remove")

# Bot response
greeting_response = ["Hi there", "hey", "How are you ? I'm good", "hello you! "]
leaving_response = ["Bye", "See you", "Come back", " Don't leave me!!! "]

def greetingCheck(sentence):
    #for word in sentence.words:
        if sentence in greeting_key :
            x = random.choice(greeting_response)
            print (x)
            return True
        else:
            print ("Sorry, I did not understand that. But Hello ")
            return False

def leavingCheck(sentence):
        if sentence in leaving_key:
            x = random.choice(leaving_response)
            print (x)
            return True
        else:
            print ("Sorry, I am lost. ")
            return False
        
############# DATABASE
def createList( sentence ):
    conn = sqlite3.connect('test1.db')
    conn.execute("INSERT INTO LISTS (NAME) VALUES (?)",(sentence));
    conn.commit()
    print (sentence," added !")
    conn.close()

def getListId(sentence):
    conn = sqlite3.connect('test1.db')
    cursor = conn.execute("SELECT ID, NAME from LISTS WHERE NAME LIKE ?",(sentence))
    for row in cursor:
       print ("Me ",row[0],". ", row[1], "\n")
    conn.close()
    return row[0]

def getList():
    conn = sqlite3.connect('test1.db')
    cursor = conn.execute("SELECT ID, NAME from LISTS")
    for row in cursor:
       print (row[0],". ", row[1], "\n")
    conn.close()
    
def deleteList( name ):
    conn = sqlite3.connect('test1.db')
    conn.execute("DELETE from LISTS where NAME = ?",(name))
    conn.commit()
    print ("Delete successful")
    conn.close()
    
def addItem( sentence, List):
    lid = getListId(List)
    conn = sqlite3.connect('test1.db')
    conn.execute("INSERT INTO ITEMS (NOM,IDL) VALUES (?,?)",(sentence,lid));
    conn.commit()
    print (sentence," added ! \n")
    conn.close()
    
def getItem(List):
    lid = getListId(List)
    i=1
    conn = sqlite3.connect('test1.db')
    cursor = conn.execute("SELECT ID, NAME from ITEMS WHERE IDL = ?",(name,lid))
    for row in cursor:
       print (i,". ", row[1], "\n")
       i = i+1
    conn.close()

    
def deleteItem( name, text ):
    lid = getListId(text)
    conn = sqlite3.connect('test1.db')
    conn.execute("DELETE from ITEMS where NOM = %s AND IDL = ?",(name,lid))
    conn.commit()
    print ("Delete successful")
    conn.close()
    
#create table
def dbinit():
    onn = sqlite3.connect('test1.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS LISTS
         (ID INTEGER PRIMARY KEY  AUTOINCREMENT ,
          NAME  TEXT    NOT NULL );''')
    conn.execute('''CREATE TABLE IF NOT EXISTS ITEMS
         (IDI INTEGER PRIMARY KEY AUTOINCREMENT,
          IDL INT NOT NULL,
          NOM  TEXT    NOT NULL );''')
    conn.close()

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

#init database
dbinit()

############################# Main
r = sr.Recognizer()
end = 1
lang = 'en'

#while True:
print ('listening')
text = listening()
greetingCheck(text)
#if(greetingCheck(text)): break
        
while (end == 1):

    print ("What do you want to do with your list? ( create, show, delete)")
    text = listening()
    #if( Checkword("list", text)):
    if( CheckactionAdd(text)):
        print ("Enter the name of your list")
        name = listening()
        createList(name)
    if( CheckactionGet(text)):
        getList()
    if(CheckactionDel(text)):
        print ("Enter the name of your list")
        name = listening()
        deleteList(name)
    if(leavingCheck(text)):
        end = 0
    print (" Do you want to play with items in your list ? say yes or no")
    text = listening()
    if( Checkword("yes", text)):
        print ("Which list?")
        listname = listening()
        print ("What do you want to do ? (add, show,delete)")
        text = listening()
        if( CheckactionAdd(text)):
            print ("Say the name of your item to add")
            name = listening()
            addItem(name, listname)
        if( CheckactionGet(text)):
            getItem(listname)
        if(CheckactionDel(text)):
            print ("Say the name of the item to delete")
            name = listening()
            deleteItem(name, listname)
        if(leavingCheck(text)):
            end = 0

            

