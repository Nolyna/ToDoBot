from tkinter import *


root = Tk()
LF = Frame(root, width = 250)
LR = Frame(root, width = 300)
todoList = []
#functions
def readWord(myList , w):
    greeting_response = ["Hi there", "hey", "How are you ? I'm good", "hello you! "]
    leaving_response = ["Bye", "See you", "Come back", " Don't leave me!!! "]

    if( w == 'add' or "create" or w == "new" or w =="more" ):
        myList.append(w)
        botSay.set(w," Added" )
    elif( w == "hello" or w == "hi" or w == "greetings" or w == "sup"):
        x = random.choice(greeting_response)
        botSay.set(x )
    elif( w == "bye" or w == "end" or w == "finish" or w == "over" or w == "leaving"):
        x = random.choice(leaving_response)
        botSay.set(x)
    elif( w == "get" or w =="show" or w == "give"):
         count = 0
         x = ""
         for item in myList:
             count+1
             x +=  item,"\n"
         botSay.set(x)
    elif( w == "delete" or w == "remove"):
        myList.remove(name)
        botSay.set(w," Removed")
    elif( w == "how many" or w == "many" or w == "much" or w == "how" or w == "number"):
        botSay.set(" You have: ",len(myList))
    elif( w == "into" or w == "exist" or w == "inside"):
        x = name in myList
        if(x): botSay.set(name," exist")
        else: botSay.set(name," does not exist")
    else:
        botSay.set("Oups!! Unkwown command" )

def click():
    x = Input.get()
    readWord(todoList, x)

#variables
botSay = StringVar()
c = """To say hi: hello, hi, greetings, sup \n
    To finish: bye, end, finish, over, leaving \n
    To add items: create,new,add,more\n
    To show list: get,show,give\n To remove element: delete,remove\n
    To get the number of elements: how many,many, much, how, number\n
    To see if items exist: into,exist, inside\n"""
    
botSay.set("Enter command")
Input = Entry(LR, bd =2, width = 20)
Text = Label(LF, text = "Commands", bd=1,relief=FLAT )
botText = Label(LR, textvariable = botSay,width = 30, height=10, bd=1,relief=SUNKEN )
B = Button(LR, text ="send", command = click)

botText.grid(row = 0)
Input.grid(row=1)
B.grid(row = 1, column=1)

LF.pack( side = LEFT)
LR.pack( side = RIGHT)


Text.pack()
root.mainloop()
