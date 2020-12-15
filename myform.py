import tkinter
import io
import os
import matplotlib.pyplot as plt
import sys
import operator
import argparse
from tkinter import *
from time import time
import matplotlib.pyplot as plt
import numpy as np
 


window = tkinter.Tk()
window.title("Word Sequence Prediction, by Henok Solomon")
#window.resizable(0,0)

iptext =  "ሄኖክ"
start_time = end_time = 0
myfilename =  "amhbig.txt"
def function():
 
    inputFilepath  =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    filename_w_ext = os.path.basename(inputFilepath)
    myfilename = os.path.splitext(filename_w_ext)
    myfilename = "".join(myfilename)
    print (myfilename)
    pass

"""
mw = tk.Tk()              #Here I tried (1)
mw.title('The game')

back = tk.Frame(master=mw, width=500, height=500, bg='black')
back.pack()
"""
	
	

# creating a root menu to insert all the sub menus
root_menu = tkinter.Menu(window)
window.config(menu = root_menu)

# creating sub menus in the root menu
file_menu = tkinter.Menu(root_menu) # it intializes a new su menu in the root menu
root_menu.add_cascade(label = "File", menu = file_menu) # it creates the name of the sub menu
file_menu.add_command(label = "New file.....", command = function) # it adds a option to the sub menu 'command' parameter is used to do some action
file_menu.add_command(label = "Open files", command = function)
file_menu.add_separator() # it adds a line after the 'Open files' option
file_menu.add_command(label = "Exit", command = window.quit)

# creting another sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = function)
edit_menu.add_command(label = "Redo", command = function)


#---------------------------------------------------------------------------------------



w = Label(window, text="Ambo University\n Department of Technology\n------------------------------- \nNLP Project Done by Henok Solomon\nhanoose212@gmail.com\n+251910330657",font = ('Sans','12','bold'), bg="red", fg="white", width=110, height=6)
w.pack(fill=X,padx=3)
w = Label(window, text="Submitted to Dr. Raja",font = ('Sans','8','bold'), bg="red", fg="white", width=110, height=3)
w.pack(fill=X,padx=3)
w = Label(window,fg="white", width=110, height=1)
w.pack(fill=X,padx=3)
w = Label(window, text="Wright Your Text Here/ፅሁፎን ኢዚህ ይፃፉ [Press Enter/ይመነ ይቻኑ]",font = ('Sans','8','bold'), bg="white", fg="Black", width=110, height=1)
w.pack(fill=X,padx=3)
"""
#Label(text="Hello", relief=RIDGE,width=15).grid(row=2,column=0)
w = Label(window, text="red", bg="red", fg="white")
w.pack(padx=5, pady=30, side=LEFT)
w = Label(window, text="green", bg="green", fg="black")
w.pack(padx=5, pady=30, side=LEFT)
w = Label(window, text="blue", bg="blue", fg="white")
w.pack(padx=5, pady=30, side=LEFT)
"""
e = Entry(window, width=30,font = ('Visual Geez Unicode','8','bold'))#.encode('utf-8')
e.pack(fill=X,padx=5, pady=20, side=TOP)
e.focus_set()
e.delete(0, END)
e.insert(0, "እኛ" )
iptext = e.get() #"መቀጮ"
fww = open("MyTimeLog.txt","w+", encoding="utf8") 
start_time = end_time = 0
f1=""
def handleReturn(event):
 fww = open("MyTimeLog.txt","w+", encoding="utf8") 
 print ("return: event.widget is",event.widget)
 print ("focus is:", window.focus_get())
 textt = e.get().encode('utf-8')
 iptext = e.get().encode('utf-8')
 print("old ",iptext)
 iptext = e.get().split(" ")[-1]
 print("new ",iptext)
#******************************count here
 print ("pressed", repr(event.char))
 end_time = time()
 print ("measured time:", end_time-start_time)
 fww.write("Time: "+str(end_time-start_time)+"\n")
 #e.bind("<Key>", key)
 #fww.close()
 

#*****************************count stops here

 
#******************************************************************************************************
 print("55*******************************************")#text search and sort
#iptext = e.get() #"መቀጮ"
 t = open(myfilename, 'rU', encoding='utf-8')
 val= []
 vald = []
 va = []
 for line_no, line in enumerate(t):
  for aline in t:
   # print(aline)
    val.append(aline.split())#all lines chopped list

 #print(val)
 print("133*******************************************")
 em = "/n"
 for p, g in enumerate(val):
        if g[1]== iptext:#if eequall toooooooooooooooooooooooo 
          #vald.append(p+2)
          vald.append((' ').join(g))
          #vald.append(' ')
          #vald.append(g.strip("\n"))
          print("the index: ",p,"The value ",(" ").join(g),(" ").join(""))
          print(p)
 print("Iptext = ",iptext)

 vald = '\n'.join(vald)+''.join(" ")
 print("199*******************************************")
 print(vald)
 print("144*******************************************")
 
 fo= open("output.txt","w+", newline='',encoding=('utf=8'))
 fo.write(vald)
 fo.close()
 #print(sorted(va, key=lambda x:int(re.match(r'(\d+)',x).groups()[0]), reverse=True))#key=lambda x:int(re.match(r'(\d+)',x).groups()[0])
 fi = open('output.txt', 'rU',encoding = ('utf-8'))
 ll = fi.readlines()
 list = sorted(ll, key=lambda x:int(re.match(r'(\d+)',x).groups()[0]), reverse=True)
 for item in list:
    print(item)
 print("88******************************************")
 #print(""+value)
 for aline in list:
     values = aline.split()
     print(values[2])


 print("00 end*****************************************")#new code end here serarch and sort



#******************************************************************************************************
 
 """#f  = io.open('txt.txt', 'rU', encoding='utf-8')
 f = open("output.txt", "r", encoding="utf8")
 fl = f.read
 value = f.readline()
 values = value.split()
 #fl = f.readlines()
 fl = f.readline()                                    
 #print(""+f1)"""
 j=7
 listbox.delete(0,END)
 for aline in list:
   values = aline.split()
   #print(values[1])Iptext =  መቀጮ
   listbox.insert(j, values[2])
   j= j-1
   print(j)
 end_time = time()
 #fww.write("Time:")
 #fww.write(str("\n",str(end_time-start_time)))
 #speedE2 = 'Speed -{}'.format(end_time-start_time)
 #fww.write(speedE2+"ddd")
 #e.bind("<Key>", key)
e.bind("<Return>", handleReturn)
"""f1=""
qbfile = open("txt.txt", "r", encoding="utf8")
def handleReturn(event):

 print ("return: event.widget is",event.widget)
 print ("focus is:", window.focus_get())
 textt = e.get().encode('utf-8')
 
 print(textt)
 f  = io.open('txt.txt', 'rU', encoding='utf-8')
 fl = f.read
 #fl = f.readlines()
 fl = f.readline()
 print(""+f1)
 
 #for aline in qbfile:
 #value = qbfile.readline()
 #values = vimport matplotlib.pyplot as plt
import numpy as np

from matplotlib import pyplot;
from pylab import genfromtxt; alue.split()
 listbox.insert(END, fl)
 #listbox.insert(END, "easy busy")
    #print('QB ', values[0] , values[1], values[2] )
	
 qbfile.close()
 
 
e.bind("<Return>", handleReturn)
"""
print("but start*************************************")

def main1():
    #word_freq(args.word, args.filename)
  word_freq(iptext , myfilename)

def word_freq(word, filename):
    doc = {}

    for line in open(filename, encoding="utf8"):

        # Assume each word is separated by a space
        split = line.split(' ')
        for entry in split:
            if (doc.__contains__(entry)):
                doc[entry] = int(doc.get(entry)) + 1
            else:
                doc[entry] = 1

    if (word not in doc):
        sys.stderr.write("Error: " + word + " does not appear in " + filename)
        sys.exit(1)

    sorted_doc = (sorted(doc.items(), key=operator.itemgetter(1)))[::-1]
    just_the_occur = []
    just_the_rank = []
    word_rank = 0
    word_frequency = 0

    entry_num = 1
    for entry in sorted_doc:

        if (entry[0] == word):
            word_rank = entry_num
            word_frequency = entry[1]

        just_the_rank.append(entry_num)
        entry_num += 1
        just_the_occur.append(entry[1])

    plt.title("Word Frequencies in " + filename)
    plt.ylabel("Total Number of Occurrences")
    plt.xlabel("Rank of word(\"" + word + "\" is rank " + str(word_rank) + ")")
    plt.loglog(just_the_rank, just_the_occur, basex=10)
    plt.scatter(
        [word_rank],
        [word_frequency],
        color="orange",
        marker="*",
        s=100,
        label=word
    )
    plt.show()


print("but end *************************************")

b = tkinter.Button(window, text="Show Graph" , bg="red", fg="white", width=10, height=1, command = main1)
b.pack(padx=8, pady=30, side="bottom")




#c = tkinter.Button(window, text ="Hello", command = helloCallBack)
#c.pack(padx=10, pady=40, side="bottom")


print("button fucked")
"""
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack()#(side = "bottom")

btn1 = tkinter.Button(top_frame, text = "Reset", fg = "red").pack()# 'fg - foreground' is used to color the contents
"""


#---------------------------------------------------------------------------------------

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print ('You selected item %d: "%s"' % (index, value))
    s = e.get()
    #e.delete(END)
    e.delete(0, END)
    e.insert(0, s+" "+value)
    iptext = value
     
#, width=55, height=15

listbox = Listbox(window)
listbox.pack(fill=X,padx=5, pady=20, side=TOP)
listbox.bind('<<ListboxSelect>>', onselect)
print("seleted list from box",listbox.get(ANCHOR))



"""
listbox.insert(END, "Predicted words")

for item in ["አንደኛ", " ሁለተኛ", "ሶስተኛ", " አራተኛ"]:
    listbox.insert(END, item)

	"""
	

# now, create some widgets in the top_frame and bottom_frame
"""
def handleReturn(event):
print "return: event.widget is",event.widget
print "focus is:", root.focus_get()

e.bind("<Return>", handleReturn)
text = e.get()
"""

window.mainloop()
