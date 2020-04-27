from tkinter import *
import json
from difflib import get_close_matches
import tkinter.messagebox

data = json.load(open("data.json"))

window = Tk()

window.configure(bg='#81de90')

window.title("Dictionary")

def dictionary():
    word = e1.get()
    word = word.lower()
    if len(e1.get()) == 0:
        tkinter.messagebox.showinfo("Empty", "Enter word to search!")
    else:
        if word in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word])
        elif word.title() in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word.title()])  
        elif word.upper() in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word.upper()])   
        elif len(get_close_matches(word, data.keys())) > 0:
            getWord = get_close_matches(word, data.keys())[0]
            ask = tkinter.messagebox.askquestion("Word not found", "Trying to search %s? " % getWord)
            # ask = ask.lower()
            if ask == 'yes':
                txt.delete("1.0", END)
                txt.insert(END, data[getWord])
            else:
                tkinter.messagebox.showerror("No such word", "There is no such word as %s " % word)
        else:
            tkinter.messagebox.showerror("No such word", "There is no such word as %s " % word)
            
def clear():
    e1.delete("0", END)
    txt.delete("1.0", END)

def close():
    get = tkinter.messagebox.askquestion("Exit", "Do you want to exit?")
    if get == 'yes':
        window.destroy()

l1 = Label(window, bd=5, font="Times 13", text="Enter word you want to search: ", fg="#000000", bg='#81de90')
l1.grid(row=0, column=0, columnspan=2)

text=StringVar()
e1 = Entry(window, bd=2, textvariable=text, width=30, fg="#000000", bg='#81de90')
e1.grid(row=0, column=2)

b1 = Button(window, bd=4,  font="Times 10", text="Search", width=25, fg="#000000", command=dictionary)
b1.grid(row=1, column=2)

b2 = Button(window, bd=4, font="Times 10", text="Clear", width=15, fg="#000000", command=clear)
b2.grid(row=1, column=1)

b3 = Button(window, bd=4, font="Times 10", text="Close", width=15, fg="#000000", command=close)
b3.grid(row=1, column=0)

txt=Text(window, height=11, width=53, wrap=WORD, fg="#000000", bg='#81de90')
txt.grid(row=2, column=0, rowspan=6, columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=6)

txt.configure(yscrollcommand=sb1.set)
sb1.configure(command=txt.yview)

txt.bind('<<TextSelect>>')

window.mainloop()
