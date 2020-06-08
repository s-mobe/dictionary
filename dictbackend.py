import json
from difflib import get_close_matches
import re
from tkinter import *


data = json.load(open("dictionary.json"))

def findWord(w):

    w = w.lower()
    if w.lower() in data:
        return (data [w.lower()])

    elif w.upper() in data:
        return (data[w.upper()])

    elif w.title() in data:
        return (data[w.title()])

    elif len(get_close_matches(w,data.keys())) > 0:
        prob = get_close_matches(w,data.keys(), cutoff= 0.8)
        return ("did you mean %s instead ? "%prob[0])
        
    else:
        return("word does not exist please try again")


def searchcommand():
    word=findWord(e1_value.get())
    lb.delete("1.0","end")
    list1 = re.split(r"\d",word)
    for item in list1:
        lb.insert(END,item + "\n")
    


window = Tk()
window.geometry("570x440")
window.wm_title("Dicitionary")

l1 = Label(window, text="enter word")
l1.grid(row=0,column=1)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)

lb = Text(window,height=22,width=70)
lb.grid(row=3,column=0,columnspan=5,rowspan=6)

b1=Button(window,text="search",width=10,command=searchcommand)
b1.grid(row=0,column=3)


window.mainloop()