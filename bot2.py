from tkinter import *


root = Tk()
import random
LF = Frame(root, width = 250)
LR = Frame(root, width = 300)
todoList = []

#functions
def readWord(w):
        global botSay
        global todoList
        print(w)

        words = w.split()
        size = len(words)

        if(size == 1):
            w = w.strip()
            greeting_response = ["Hi there", "hey", "How are you ? I'm good", "hello you!"]
            leaving_response = ["Bye", "See you", "Come back", " Don't leave me!!! "]
            jokes_r = ["I like to hold hands at the movies... \n which always seems to startle strangers","The three most beautiful words \n in our common language? \n  I am amazing.","What happens to a frog's car \n when it breaks down? \n It gets toad away."]

            if( w == 'add' or  w =='create' or w == 'new' or w == 'more' ):
                botSay.set(" Enter item" )
                Input1.grid()
                Input.grid_remove()
                C.grid()
                B.grid_remove()
            elif( w == 'hello' or w == 'hi' or w == 'greetings' or w == 'sup'):
                x = random.choice(greeting_response)
                botSay.set(x)
            elif( w == 'bye' or w == 'end' or w == 'finish' or w == 'over'or w == 'leaving'):
                x = random.choice(leaving_response)
                botSay.set(x)
            elif( w == 'joke'):
                x = random.choice(jokes_r)
                botSay.set(x)
            elif( w == 'get' or w =='show' or w == 'give'):
                 count = 0
                 x = " My List: \n"
                 p = " \n "
                 for item in todoList:
                     count+1
                     x = x + item
                     x = x + p
                 print (todoList)
                 botSay.set(x)
            elif( w == 'delete' or w == 'remove'):
                botSay.set(" Enter item" )
                Input2.grid()
                Input.grid_remove()
                D.grid()
                B.grid_remove()
            elif( w == 'how many' or w == 'many' or w == 'much' or w == 'how' or w == 'number'):
                x = " You have: ",len(todoList),"elements in your list. \n Enter command"
                botSay.set(x)
            elif( w == 'into' or w == 'exist' or w == 'inside'):
                botSay.set(" Enter item" )
                Input3.grid()
                Input.grid_remove()
                F.grid()
                B.grid_remove()
            else:
                botSay.set("Oups!! Unkwown command" )
        else:
            v = ""
            w = words[0]
            for i in words[1:]:
                v = v+i
            print ("v",v)
            if( w == 'add' or  w =='create' or w == 'new' or w == 'more' ):
                todoList.append(v)
                botSay.set(" Added. \n Enter command" )
            elif( w == 'delete' or w == 'remove'):
                todoList.remove(v)
                botSay.set("Removed. \n Enter command")
            elif( w == 'into' or w == 'exist' or w == 'inside'):
                Z = v in todoList
                strs1 = v,"exist. \n Enter command"
                strs2 = v," does not exist. \n Enter command"
                if(Z): botSay.set(strs1)
                else: botSay.set(strs2)
            else:
                botSay.set("Oups!! Unkwown command" )

def click():
    global todoList
    x = Input.get()
    readWord(x)
    Input.delete(0, 'end')
def click2():
    global todoList
    x = Input2.get()
    Input2.delete(0, 'end')
    todoList.remove(x)
    botSay.set("Removed. \n Enter command")
    print(todoList)
    Input.grid()
    Input2.grid_remove()
    B.grid()
    D.grid_remove()

def click3():
    global todoList
    x = Input3.get()
    Input3.delete(0, 'end')
    Z = x in todoList
    strs1 = x,"exist. \n Enter command"
    strs2 = x," does not exist. \n Enter command"
    if(Z): botSay.set(strs1)
    else: botSay.set(strs2)
    Input.grid()
    Input3.grid_remove()
    B.grid()
    F.grid_remove()

def click1():
    global todoList
    x = Input1.get()
    Input1.delete(0, 'end')
    todoList.append(x)
    botSay.set(" Added. \n Enter command" )
    print(todoList)
    Input.grid()
    Input1.grid_remove()
    B.grid()
    C.grid_remove()

#variables
botSay = StringVar()
Z = """To say hi: hello, hi, greetings, sup \n
    To finish: bye, end, finish, over, leaving \n
    To add items: create,new,add,more\n
    To show list: get,show,give\n To remove element: delete,remove\n
    To get the number of elements: how many,many, much, how, number\n
    To see if items exist: into,exist, inside\n"""
    
botSay.set("Enter command")
Input = Entry(LR, bd =2, width = 20)
Input1 = Entry(LR, bd =2, width = 20)
Input2 = Entry(LR, bd =2, width = 20)
Input3 = Entry(LR, bd =2, width = 20)

Text = Label(LF, text = Z, bd=1,relief=FLAT )
botText = Label(LR, textvariable = botSay,width = 30, height=10, bd=1,relief=SUNKEN )

B = Button(LR, text ="send", command = click)
C = Button(LR, text ="send", command = click1)
D = Button(LR, text ="send", command = click2)
F = Button(LR, text ="send", command = click3)

botText.grid(row = 0)
Input.grid(row=1)
B.grid(row = 1, column=1)

LF.pack( side = LEFT)
LR.pack( side = RIGHT)


Text.pack()
root.mainloop()
